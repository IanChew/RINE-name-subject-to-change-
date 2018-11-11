# WIP Instant Messanging Program

## Feature Roadmap:
### Implemented:
* Basic message sending and receiving.
* Username setting.
* Asynchronous sending and receiving in the client (buggy).
* File sharing.
* Some degree of graceful disconnecting.
* Connection and disconnection messages.

### Future features (in rough order to implement them):
* Fixing the (visual) client bug where if you receive a message while typing one out, it interrupts your buffer.
* Protocol formalization.
* Better handling of errors in general.
 * If the server disconnects, the client should exit with an error message instead of the input thread just dying.
* Safer file sharing.
 * Support for large files, since they currently crash the server.
 * Let the user decide whether to save a file or not.
 * Let the user decide whether to even receive the file in the first place.
 * Let the user decide where to save the file.
 * Prevent the file from begin saved in unsafe places by default.
* More robust file sharing.
* Persistence (database?).
 * Retrieving past messages from the server when the client wants them.
 * Sending messages to users that are offline.
* Authentication (might need to come after persistance).
* Synchronizing the clients when a user is logged in on the same username but on multiple computers.
* Encryption (end-to-end).
* Multiple chat rooms/private chats.
* Self-destructing messages, that disappear after a certain amount of time.
 * Once the server is persistent, we can also delete the message off the server.
* GUI support.
* Thumbnail images with the option to download the full image.
* Web/Mobile client.

