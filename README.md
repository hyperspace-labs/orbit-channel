# Orbit Channel 

A decentralized registry of released ip by Hyperspace Labs for [Orbit](https://github.com/cdotrus/orbit), an agile package manager and extensible build tool for hardware description languages (HDLs).

## Installing

To access the configurations and get the most out of these settings, you should at least have `git` installed and found on your system's PATH.

1. Download the profile from its remote repository using `git`:

```
git clone https://github.com/hyperspace-labs/orbit-channel.git "$(orbit env ORBIT_HOME)/channels/hyperspace-labs"
```

2. Link the channel in the home configuration using `orbit`:

```
orbit config --append include="channels/hyperspace-labs/config.toml"
```
