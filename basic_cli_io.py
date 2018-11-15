import baseio
import readline # get_line_buffer

# Basic CLI I/O class that is supported on any platform.
class BasicCLIIO(baseio.BaseIO):
	def print(self, *args, **kwargs):
		# Get the current buffer of non-accepted input.
		buffer = readline.get_line_buffer()
		if len(buffer) != 0:
			# Write the message over the current buffer,
			# shift the line up with newline, then write

			# First create the message to print:
			sep = ' '
			if ('sep' in kwargs):
				sep = kwargs['sep']
			message = sep.join(args)

			# Then print it, as described above.
			print("\r" + message + "\n" + buffer, end = '', **kwargs)
		else:
			print(*args, **kwargs)

	# Gets a string from the user.
	def input(self, prompt = ""):
		return input(prompt)

