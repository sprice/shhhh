# shhhh

shhhh is a tool to transcribe audio using [OpenAI Whisper](https://openai.com/blog/whisper/)

##

This project currently assumes you're using a Mac and are comfortable using the Terminal.

Future versions of shhhh will be easier to set up.

## Installation

### Install Developer Tools

In your terminal, execute the following command. Note this will download and install approximately 1.5GB of software.

```sh
$ xcode-select --install
```

### Install Homebrew

Installation instructions are on the [Homebrew](https://brew.sh/) website.

### Install ffmpeg

In your terminal, execute the following command.

```sh
$ brew install ffmpeg
```

### Install pydub

In your terminal, execute the following command.

```sh
$ pip3 install pydump
```

### Install Whisper

In your terminal, execute the following command.

```sh
$ pip3 install git+https://github.com/openai/whisper.git
```

### Ensure your Python Certificates are happy

See [this StackOverflow post](https://stackoverflow.com/a/70495761)

## Usage

Place a file named `original.mp3` into the directory of this code.

### Prepare audio

In your terminal, execute the following command.

```sh
$ make prepare
```

### Transribe audio

In your terminal, execute the following command.

```sh
$ make transcribe
```

## Thanks

Thanks to the [first result](https://eslyes.com/easydialogs/ec/entertainment01.htm) I was able to Google with a short audio mp3.

Thanks to [Konstantin Rink](Konstantin Rink) and [this article](https://towardsdatascience.com/transcribe-audio-files-with-openais-whisper-e973ae348aa7) for the bulk of the code.
