from abc import ABCMeta
import pickle

from kafka import KafkaProducer


class Producer(metaclass=ABCMeta):
    """ Class to inherit from if your class needs to publish events (KafkaProducer).
        This class assumes that A Producer will publish to only one topic. This is a nice
        convention to follow in order to separate logic and to follow the MicroServices
        Architecture.
    """

    def __init__(self):
        super().__init__()
        self.producer = KafkaProducer(bootstrap_servers=["localhost:9092"])

    def send(self, output_topic_class, msg):
        """

        :param output_topic_class:
        :param msg: The message to send. It can be an instance of any class.
        """
        serialized_msg = pickle.dumps(msg, pickle.HIGHEST_PROTOCOL)
        output_topic = output_topic_class.__name__
        self.producer.send(output_topic, serialized_msg)
        self.producer.flush()
