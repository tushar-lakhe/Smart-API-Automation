package examples.users;

import org.apache.kafka.clients.producer.Callback;
import org.apache.kafka.clients.producer.KafkaProducer;
import org.apache.kafka.clients.producer.ProducerConfig;
import org.apache.kafka.clients.producer.ProducerRecord;
import org.apache.kafka.clients.producer.RecordMetadata;
import org.apache.kafka.common.serialization.StringSerializer;
import org.apache.kafka.common.security.scram.ScramLoginModule;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.util.Properties;
import java.util.concurrent.ExecutionException;

public class Kafka {
	public static KafkaProducer<String, String> producer;
	public static Logger logger = LoggerFactory.getLogger(Kafka.class);
	
	/**
	* Connects producer with kafka broker.
	* @param bootstrapServers Kafka Bootstrap Servers comma separated list.  
	*/
	public static void connect(String bootstrapServers) {
		Properties properties = new Properties();
		properties.setProperty(ProducerConfig.BOOTSTRAP_SERVERS_CONFIG, bootstrapServers);
		properties.setProperty(ProducerConfig.KEY_SERIALIZER_CLASS_CONFIG, StringSerializer.class.getName());
		properties.setProperty(ProducerConfig.VALUE_SERIALIZER_CLASS_CONFIG, StringSerializer.class.getName());
		producer = new KafkaProducer<String, String>(properties);
	}
	/**
	* Connects producer with kafka broker with clientId.
	* @param bootstrapServers Kafka Bootstrap Servers comma separated list. 
	* @param clientId Client Id for kafka connection. 
	*/
	public static void connect(String bootstrapServers, String clientId) {
		Properties properties = new Properties();
		properties.setProperty(ProducerConfig.BOOTSTRAP_SERVERS_CONFIG, bootstrapServers);
		properties.setProperty(ProducerConfig.CLIENT_ID_CONFIG, clientId);
		properties.setProperty(ProducerConfig.KEY_SERIALIZER_CLASS_CONFIG, StringSerializer.class.getName());
		properties.setProperty(ProducerConfig.VALUE_SERIALIZER_CLASS_CONFIG, StringSerializer.class.getName());
		producer = new KafkaProducer<String, String>(properties);
	}
	/**
	* Connects producer with kafka broker with SASL_PLAINTEXT protocol.
	* @param bootstrapServers Kafka Bootstrap Servers comma separated list. 
	* @param username Username for kafka connection. 
	* @param password Password for kafka connection.
	*/
	public static void connect(String bootstrapServers, String username, String password) {
		username = username == null ? "" : username;
		password = password == null ? "" : password;
	    
		Properties properties = new Properties();
		properties.setProperty(ProducerConfig.BOOTSTRAP_SERVERS_CONFIG, bootstrapServers);
		properties.setProperty(ProducerConfig.KEY_SERIALIZER_CLASS_CONFIG, StringSerializer.class.getName());
		properties.setProperty(ProducerConfig.VALUE_SERIALIZER_CLASS_CONFIG, StringSerializer.class.getName());
		
		properties.setProperty("security.protocol", "SASL_PLAINTEXT");
		properties.setProperty("sasl.mechanism", "SCRAM-SHA-512");
		properties.setProperty("sasl.jaas.config", "org.apache.kafka.common.security.scram.ScramLoginModule required username=\"" + username + "\" password=\"" + password + "\";");
		logger.info("Configured kafka connection with SASL_PLAINTEXT protocol " );
		
		producer = new KafkaProducer<String, String>(properties);
	}
	/**
	* Connects producer with kafka broker with SSL protocol.
	* @param bootstrapServers Kafka Bootstrap Servers comma separated list. 
	* @param truststoreLocation Truststore JKS file location for kafka connection. 
	* @param truststorePassword Truststore JKS file password for kafka connection.
	* @param keystoreLocation Keystore JKS file location for kafka connection.
	* @param keystorePassword Keystore JKS file password for kafka connection.
	* @param keyPassword Key password for kafka connection.
	*/
	public static void connect(String bootstrapServers, String truststoreLocation, String truststorePassword, String keystoreLocation, String keystorePassword, String keyPassword) {
		Properties properties = new Properties();
		properties.setProperty(ProducerConfig.BOOTSTRAP_SERVERS_CONFIG, bootstrapServers);
		properties.setProperty(ProducerConfig.KEY_SERIALIZER_CLASS_CONFIG, StringSerializer.class.getName());
		properties.setProperty(ProducerConfig.VALUE_SERIALIZER_CLASS_CONFIG, StringSerializer.class.getName());
		
		properties.setProperty("security.protocol", "SSL");
		properties.setProperty("ssl.protocol", "TLSv1.2");
		properties.setProperty("ssl.truststore.location", truststoreLocation);
		properties.setProperty("ssl.truststore.password", truststorePassword);
		properties.setProperty("ssl.keystore.location", keystoreLocation);
		properties.setProperty("ssl.keystore.password", keystorePassword);
		properties.setProperty("ssl.key.password", keyPassword);
		logger.info("Configured kafka connection with SSL protocol" );
		
		producer = new KafkaProducer<String, String>(properties);
	}
	/**
	* Connects producer with kafka broker with SASL_SSL protocol.
	* @param bootstrapServers Kafka Bootstrap Servers comma separated list. 
	* @param truststoreLocation Truststore JKS file location for kafka connection. 
	* @param truststorePassword Truststore JKS file password for kafka connection.
	* @param username Username for kafka connection. 
	* @param password Password for kafka connection.
	*/
	public static void connect(String bootstrapServers, String truststoreLocation, String truststorePassword, String username, String password) {
		username = username == null ? "" : username;
		password = password == null ? "" : password;
		
		Properties properties = new Properties();
		properties.setProperty(ProducerConfig.BOOTSTRAP_SERVERS_CONFIG, bootstrapServers);
		properties.setProperty(ProducerConfig.KEY_SERIALIZER_CLASS_CONFIG, StringSerializer.class.getName());
		properties.setProperty(ProducerConfig.VALUE_SERIALIZER_CLASS_CONFIG, StringSerializer.class.getName());
		
		properties.setProperty("security.protocol", "SASL_SSL");
		properties.setProperty("ssl.protocol", "TLSv1.2");
		properties.setProperty("ssl.truststore.location", truststoreLocation);
		properties.setProperty("ssl.truststore.password", truststorePassword);
		properties.setProperty("ssl.protocol", "TLS");
		properties.setProperty("sasl.mechanism", "SCRAM-SHA-512");
		properties.setProperty("sasl.jaas.config", "org.apache.kafka.common.security.scram.ScramLoginModule required username=\"" + username + "\" password=\"" + password + "\";");
		logger.info("Configured kafka connection with SASL_SSL protocol" );
		
		producer = new KafkaProducer<String, String>(properties);
	}
	/**
	* Push payload into givan kafka topic.
	* @param topic Kafka topic name. 
	* @param payload Payload to be send. 
	*/
	public static void send(String topic, String payload) {
		ProducerRecord<String, String> record = new ProducerRecord<String, String>(topic, payload);
		/*
		 * try { RecordMetadata metadata = producer.send(record).get();
		 * System.out.println("Record sent to partition " + metadata.partition() +
		 * " with offset " + metadata.offset()); } catch (ExecutionException e) {
		 * System.out.println("Error in sending record"); System.out.println(e); } catch
		 * (InterruptedException e) { System.out.println("Error in sending record");
		 * System.out.println(e); }
		 */
		producer.send(record, new Callback() {
			public void onCompletion(RecordMetadata recordMetadata, Exception e) {
				//Logger logger = LoggerFactory.getLogger(Kafka.class);
				if (e == null) {
					logger.info("Successfully received the details as: \n" + "Topic:" + recordMetadata.topic() + "\n"
							+ "Partition:" + recordMetadata.partition() + "\n" + "Offset" + recordMetadata.offset()
							+ "\n" + "Timestamp" + recordMetadata.timestamp());
				} else {
					logger.error("Can't produce, getting error", e);
				}
			}
		});
	}
	/**
	* Disconnect the kafka server with a flush. 
	*/
	public static void disconnect() {
		producer.flush();
		producer.close();
	}
}
