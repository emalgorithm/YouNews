from abc import ABCMeta, abstractmethod
import pickle

from kafka import KafkaConsumer


class Consumer(metaclass=ABCMeta):
    """ Class to inherit from if your class needs to listen for events (KafkaConsumer).
        This class assumes that a Producer will consume from only one topic. This is a nice
        convention to follow in order to separate logic and to follow the MicroServices
        Architecture.
    """

    def __init__(self, event_class):
        super().__init__()
        self.consumer = KafkaConsumer(event_class.__name__, bootstrap_servers=["localhost:9092"])
        # self.consumer.seek_to_end()

    def run(self):
        for serialized_msg in self.consumer:
            msg_value = pickle.loads(serialized_msg.value)
            self.on_received_message(msg_value)

    @abstractmethod
    def on_received_message(self, msg):
        raise NotImplementedError("Should implement " + self.on_received_message.__name__)