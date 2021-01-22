# Senator Grassley Schedule Emailer

[Senator Grassley](https://en.wikipedia.org/wiki/Chuck_Grassley) is well known for his 99 County Tour. However, the dates and times of these meetings are frequently scheduled without much lead time. They are also usually during business hours on weekdays.

See [here](https://davidbody.github.io/grassley-townhalls/) for more details on how Senator Grassley avoids meetings in areas that may be less inviting to him.

So I may attend one close by me this lambda will send me daily emails of his schedule.

## Build & Deploy

This project uses python and AWS SAM to build and deploy.

```bash
sam build -u
```

```bash
sam deploy --guided
```