# runfn-switchboard

long running google cloud run function.

connects remote controls with [radio-pad](https://github.com/briceburg/radio-pad) to receive the currently playing station.

  * radio-pad broadcasts the currently playing station to the 'station-playing' channel.
  * remote controls listen for changes and update their UI

uses reconnecting websockets between cloud function and client apps (remote controls).

deployed via `bin/deploy`
