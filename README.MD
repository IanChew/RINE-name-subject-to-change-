# WIP Instant Messanging Program

## Feature Roadmap:
### Implemented:
* Basic message sending and receiving.
* Username setting.
* Asynchronous sending and receiving in the client (buggy).
* File sharing.
  * Support for large files.
* Some degree of graceful disconnecting.
* Connection and disconnection messages.
* Fixing the (visual) client bug where if you receive a message while typing one out, it interrupts your buffer.


### Future features (in rough order to implement them):
* Protocol formalization.
* Better handling of errors in general.
  * If the server disconnects, the client should exit with an error message instead of the input thread just dying.
* Safer file sharing.
  * Support for large files handled asynchronously (client and server).
  * Let the user decide whether to save a file or not.
  * Let the user decide whether to even receive the file in the first place.
  * Let the user decide where to save the file.
  * Prevent the file from begin saved in unsafe places by default.
* Implement file persistance levels.
* Persistence (database?).
  * Retrieving past messages from the server when the client wants them.
  * Sending messages to users that are offline.
  * Have the server only send messages when the client asks for them.
* Have the client send optional read notifications to the sender when the message is read.
* Authentication (might need to come after persistance).
* Synchronizing the clients when a user is logged in on the same username but on multiple computers.
* Encryption (end-to-end).
* Multiple chat rooms/private chats.
* Self-destructing messages, that disappear after a certain amount of time.
* Sending messages back in time. (D-Mail)
 * Once the server is persistent, we can also delete the message off the server.
* GUI support.
* Add support for colour based reply system with collapse and expand support. (Reading Steiner)
* Thumbnail images with the option to download the full image.
* Web/Mobile client.

