## An analysis of the 2017 parking fines in Bonn, Germany

I absolutely love open data. Going through my city-of-residence's open data sets, I found the parking and speeding fines to be public. At a first glance, I counted 150k parking fines in only one year, totaling 2.5 million EUR. In a city of only 350k inhabitants, that's a lot. I'm parsing the data to see if I can find correlation and, why not, causation.

Already parsed data can be found here: [https://viorelsfetea.github.io/parking-fines-in-bonn](https://viorelsfetea.github.io/parking-fines-in-bonn)

*Tech stack:*
- I imported the data set in PostgreSQL, because of the complex GIS capabilities it offers ([see existing queries](https://github.com/viorelsfetea/parking-fines-in-bonn/tree/master/_data_root/queries))
- The data is parsed with Python ([see existing scripts](https://github.com/viorelsfetea/parking-fines-in-bonn/tree/master/_data_root/scripts))
- Site is built with Jekyll
- Graphs are built with Google Charts
