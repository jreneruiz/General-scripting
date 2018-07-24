# Label-printer
This script was one of the first that I did (2015 approximately) and they ended up in a production environment.

- [Label-printer](#label-printer)
- [Problem description](#problem-description)
- [Restrictions](#restrictions)
- [Solution](#solution)
- [Personal comments](#personal-comments)

# Problem description
In the organization where I worked, they made products that contained ballasts, these ballasts were programmable and they opted to buy a device to program them in terms of amperage.

![balastra](https://www.assets.lighting.philips.com/is/image/PhilipsLighting/d5ddaf37c57a46928806a64300c90d85?wid=400&hei=400&$pnglarge$)

There was a need to put a label on the ballast which served as identification, to know how much amperage was programmed. The label only contained the date and the amount of programmed amperage.

The configuration machine was connected to a computer with Windows 7 and a software of the provider, the software showed the word "ok" when the ballast finished its configuration and everything had gone well, otherwise it showed the word "fail".

The provider program created a log file for every configuration that was done.

# Restrictions
- You had to use a Zebra GK420t printer
- You had to read the contents of a file that generated the owner's software each time it was modified
- After reading the last line of the file, if the last recorded configuration had been satisfactory, print a label with the date and amperage of the ballast.
- Only had about 6 hours of development, testing and implementation in production

# Solution
A small java program was created to work as a service to identify if the configurations had been satisfactory.

It was executed at the beginning of the operating system, so that it's always available, they not affect the performance of the equipment since it was only used for this.

You can review the complete project in the following [link](https://github.com/jreneruiz/Impresor-de-etiquetas-zebra)


# Personal comments
When I made this script I was very excited, since it was beneficial for the organization, I am aware that it is not the best solution but it is what I had at hand at that moment.
