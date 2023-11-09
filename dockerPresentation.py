import streamlit as st

st.caption('Team Marquet')
st.image('https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Flogos-world.net%2Fwp-content%2Fuploads%2F2021%2F02%2FDocker-Symbol.png&f=1&nofb=1&ipt=5a14afd1e119e1ac15314fcdfdbb1773fa696a5236965cb353f443f7e97f5c97&ipo=images', width=400)

'# Docker'
st.caption('What is it? What does it do? How does it work?')

# Yes, you can just put a string here and streamlit recognizes it. It's that easy.
"""
### Docker is *not* a virtual machine.
It's also not quite emulation software. It's kind of it's own niche which it fills nicely.
Which is why it's used by over 20 million developers in more than 7 million applications.

You can kind of think of it as a lightweight virtual machine for a specific process.
"""

with st.expander('Purpose'):
    """
    The use of docker is that it allows you to set up an enviorment (*`container`*) you can run software
    in that is consistent across hardware. So you can send your friend a script you wrote, and you
    don't have to worry about it not running on their machine, because they don't have some package
    installed, or they run Windows instead of Linux, or anything like that.
    """

with st.expander('Containers and Images'):
    """
    In docker, you have several parts.
    #### Images
    Images are like a variable definition. Think of it like a C++ header file, or ...something else
    not relating to C++

    You define images by
    #### Containers
    Containers are instantiations of images.
    """

with st.expander('Integration'):
    """
    It has a fully featured VSCode extension and integrates seemlessly with GitHub
    """

with st.expander('Dockerfile'):
    """
    The heart of using Docker is the file called `Dockerfile`. In a Dockerfile, you specify the image,
    which, when instantiated, becomes a runnable container.
    Here, we'll show you the basic commands used in Dockerfiles.
    """

    st.caption('These don\'t *have* to be uppercase, but they always are by convention')

    # Docs are here: https://docs.docker.com/engine/reference/builder/#from
    """
    - `FROM`
        - Always the very first line in a file\*, it specifies the base image from the docker website
        - `<example>`
    - `RUN`
        - Runs a command from inside the container. By defualt, it uses bash on Linux, or powershell
        Windows (I think, double check this)
        - `RUN apt-get install dependant-package`
    """
    # * This isn't always true, see https://docs.docker.com/engine/reference/builder/#parser-directives
