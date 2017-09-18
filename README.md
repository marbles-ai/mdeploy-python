# Marbles deployment

Deployment helpers.

Currently we only use AWS however we can add other service providers to this package.

## Building the wheel
The wheel output will be located at `./dist`. The `release` flag can optionally set the version,
before running the script. The `clean` flag will clean the build and optionally the dist if `clean --all`.
```
python setup.py [clean [--all]] [release --version=<V.R.B>]
```

## Uploading wheel to Github

Wheels are stored on our github repository. 
Make sure you tag with the version each time you upload.

## TODO
1. Add a script to increment version, tag, and upload wheel.

