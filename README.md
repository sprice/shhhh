# shhhh

shhhh is a tool to transcribe audio using [OpenAI Whisper](https://openai.com/blog/whisper/)

##

This project currently assumes you're using a Mac and are comfortable using the Terminal.

Future versions of shhhh will be easier to set up.

## Installation

## Open up a terminal

Open up [Terminal on your Mac](https://www.howtogeek.com/682770/how-to-open-the-terminal-on-a-mac/)

### Get this code onto your computer

In Terminal, go to a folder you'd like to place this code.

```sh
cd Documents
```

Clone this git repository onto your computer.

```sh
git clone https://github.com/sprice/shhhh.git
```

### Install Developer Tools

In Terminal, execute the following command. Note this will download and install approximately 1.5GB of software.

```sh
xcode-select --install
```

### Install Homebrew

Installation instructions are on the [Homebrew](https://brew.sh/) website.

### Install ffmpeg

Homebrew is a prerequisite to install ffmpeg.

In Terminal, execute the following command.

```sh
brew install ffmpeg
```

### Install pydub

In Terminal, execute the following command.

```sh
pip3 install pydump
```

### Install Whisper

In Terminal, execute the following command.

```sh
pip3 install git+https://github.com/openai/whisper.git
```

### Ensure your Python Certificates are happy

See [this StackOverflow post](https://stackoverflow.com/a/70495761)

## Usage

Place a file named `original.mp3` into the directory of this code.

To open this directory up in Finder type the following in Terminal when you are in the folder of this code.

```sh
open .
```

### Prepare audio

In Terminal, execute the following command.

```sh
make prepare
```

### Transribe audio

In your terminal, execute the following command.

```sh
make transcribe
```

### Read your sweet new transcription

Open up `output.txt`

## Thanks

Thanks to the [first result](https://eslyes.com/easydialogs/ec/entertainment01.htm) I was able to Google with a short audio mp3.

Thanks to [Konstantin Rink](https://konstantin-rink.medium.com/) and his article [Transcribe audio files with OpenAI’s Whisper](https://towardsdatascience.com/transcribe-audio-files-with-openais-whisper-e973ae348aa7) for the bulk of the code.

Thanks to this [StackOverflow Answer](https://stackoverflow.com/a/9895195) for the addition of limiting line length in `output.txt`
