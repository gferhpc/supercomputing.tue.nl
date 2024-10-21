[![pipeline status](https://gitlab.tue.nl/hpclab/website/badges/main/pipeline.svg)](https://gitlab.tue.nl/hpclab/website/-/commits/main)

# TU/e Supercomputing Center

The official website of the TU/e Supercomputing Center (TUeSC).

## Customizations

### Backdrop / Hero frontpage

- Backdrop images should, ideally, have an aspect ratio of 16:9 (720p, 1080p etc.)

## Events

We're using a customized plugin for our events, based on the
official [mkdocs-material blog plugin](https://squidfunk.github.io/mkdocs-material/plugins/blog/). All settings listed
here a compatible, with addition of the
following [Metadata](https://squidfunk.github.io/mkdocs-material/plugins/blog/#metadata) options:

| Property        | Value                          | Description              |
|-----------------|--------------------------------|--------------------------|
| type (required) | `news`, `maintenance`, `event` | Article type (see below) | 

### Type `news`

No additional properties available. Please refer to
the [official documentation](https://squidfunk.github.io/mkdocs-material/plugins/blog/) of this plugin.

### Type `maintenance`

In addition to `news`:

| Property   | Value                              | Description                        |
|------------|------------------------------------|------------------------------------|
| date.start | YYYY-MM-DD<br/>YYYY-MM-DDTHH:II:SS | Start date/time of the maintenance | 
| date.end   | YYYY-MM-DD<br/>YYYY-MM-DDTHH:II:SS | End date/time of the maintenance   | 

### Type `event`

In addition to `news`:

| Property   | Value                                        | Description                                        |
|------------|----------------------------------------------|----------------------------------------------------|
| date.start | YYYY-MM-DD<br/>YYYY-MM-DDTHH:II:SS           | Start date/time of the event                       | 
| date.end   | YYYY-MM-DD<br/>YYYY-MM-DDTHH:II:SS           | End date/time of the event                         | 
| price      | 0.00 (free), or any other digit number       | The entree fee of the event                        |
| location   | String, Event location                       | Location of where the event will take place        |
| image      | URL or relative path from the `/docs` folder | Image shown with the event                         |
| scheme     | `autumn`, `spring`                           | Change default color scheme for the specific event |
| sponsors   | see [sponsors](#sponsors)                    | The sponsors of the event                          |
| schedule   | see [schedule](#schedule)                    | The detailed schedule of the event                 |

#### `sponsors`

| Property | Value                                        | Description            |
|----------|----------------------------------------------|------------------------|
| name     | String                                       | Name of the sponsor    |
| url      | String                                       | Website of the sponsor |
| avatar   | URL or relative path from the `/docs` folder | Logo of the sponsor    |

#### `schedule`

| Property | Value                                                                                                     | Description                 |
|----------|-----------------------------------------------------------------------------------------------------------|-----------------------------|
| start    | YYYY-MM-DD<br/>YYYY-MM-DDTHH:II:SS                                                                        | Start date/time of the item | 
| end      | YYYY-MM-DD<br/>YYYY-MM-DDTHH:II:SS                                                                        | End date/time of the item   |
| title    | String                                                                                                    | The shown title of the item |
| icon     | See [supported icons](https://squidfunk.github.io/mkdocs-material/reference/icons-emojis/){target=_blank} | Icon of the item            |
| authors  | see [authors](https://squidfunk.github.io/mkdocs-material/plugins/blog/#meta.authors){target=_blank}      | The speaker(s) of the event |
| schedule | see [schedule](#schedule)                                                                                 | The subschedule of the item |
