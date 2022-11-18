package examples.users;

import javax.jms.*;
import org.apache.activemq.ActiveMQConnectionFactory;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.io.Serializable;

public class queueUtils {

    private static final Logger logger = LoggerFactory.getLogger(queueUtils.class);


    static Connection connection;


    public static void createConnection(String ConnectionURL, String uname, String upassword) {
        try {

            String username = uname;
            String password = upassword;
            ActiveMQConnectionFactory connectionFactory = new ActiveMQConnectionFactory(username, password, ConnectionURL);
            //jndiBasedConnectionFactory = jmsJndiConnectionFactory.connectionFactoryName("ConnectionFactory").url("tcp://localhost:61616").credentials("user", "secret").contextFactory("org.apache.activemq.jndi.ActiveMQInitialContextFactory");

            connection = connectionFactory.createConnection();
            connection.start();
        } catch (Exception e) {
            throw new RuntimeException(e);
        }
    }

    public static boolean sendText(String queueName, String text, int delayMillis) {
        try {

            logger.info("*** artificial delay {}: {}", queueName, delayMillis);
            Thread.sleep(delayMillis);
            Session session = connection.createSession(false, Session.AUTO_ACKNOWLEDGE);
            Destination destination = session.createQueue(queueName);
            MessageProducer producer = session.createProducer(destination);
            producer.setDeliveryMode(DeliveryMode.PERSISTENT);
            TextMessage message = session.createTextMessage(text);
            producer.send(message);
            logger.info("*** sent message on queue {}:", queueName);
            session.close();
            connection.close();
            return true;
        } catch (Exception e) {
            throw new RuntimeException(e);
        }
    }

    public static boolean sendObject(String queueName, Object obj, int delayMillis) {
        try {

            logger.info("*** artificial delay {}: {}", queueName, delayMillis);
            Thread.sleep(delayMillis);
            Session session = connection.createSession(false, Session.AUTO_ACKNOWLEDGE);
            Destination destination = session.createQueue(queueName);
            MessageProducer producer = session.createProducer(destination);
            producer.setDeliveryMode(DeliveryMode.PERSISTENT);
            ObjectMessage message = session.createObjectMessage((Serializable) obj);
            producer.send(message);
            logger.info("*** sent message on queue {}:", queueName);
            session.close();
            connection.close();
            return true;
        } catch (Exception e) {
            throw new RuntimeException(e);
        }
    }

    public static boolean sendBytes(String queueName, byte[] bytes, int delayMillis) {
        try {

            logger.info("*** artificial delay {}: {}", queueName, delayMillis);
            Thread.sleep(delayMillis);
            Session session = connection.createSession(false, Session.AUTO_ACKNOWLEDGE);
            Destination destination = session.createQueue(queueName);
            MessageProducer producer = session.createProducer(destination);
            producer.setDeliveryMode(DeliveryMode.PERSISTENT);
            BytesMessage message = session.createBytesMessage();
            message.writeBytes(bytes);
            producer.send(message);
            logger.info("*** sent message on queue {}:", queueName);
            session.close();
            connection.close();
            return true;
        } catch (Exception e) {
            throw new RuntimeException(e);
        }
    }
}






