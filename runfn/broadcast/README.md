# runfn-broadcast

short running google cloud run function.

receives broadcast requests over HTTP and publishes them to a redis channel.

station-changing requests look like:

```sh
curl https://fn-project.region.run.app/?station={station_id}
```

currently-playing requests look like:

```sh
curl https://fn-project.region.run.app/?currently_playing={station_id}
```

deployed via `bin/deploy`
