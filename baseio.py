import abc
from abc import abstractmethod


# Abstract base class, representing the IO of the chat client.
# This contains methods for displaying what the client receives
# from the server, and taking in input to send to the server.

class BaseIO(metaclass = abc.ABCMeta):
	# Print out a string to the screen.
	@abstractmethod
	def print(self, *args, **kwargs):
		...

	# Get a string from the user, with an optional
	# prompt string.
	@abstractmethod
	def input(self, prompt = ""):
		...


