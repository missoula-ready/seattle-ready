# seattle-ready
A disaster readiness website specific to the Seattle metro area.


The project is a custom instance of the [Disaster Preparedness](https://github.com/missoula-ready/disaster-preparedness) project, which is an adaptation of [a pioneering project from Oregon](https://github.com/Oregon-Public-Broadcasting/earthquake-preparedness) but has been generalized to make it easy to clone and tailor to other regions.

# To set it up, follow the instructions in the [Disaster Preparedness project README](https://github.com/missoula-ready/disaster-preparedness/blob/master/README.md). But instead of DJANGO_SECRET_KEY, use DJANGO_SECRET_KEY_SEATTLE, and instead of DATABASE_URL, use DATABASE_URL_SEATTLE.

Depending on your server setup, you may want to put these values in settings.py directly.

# Values to put in Django Admin

### Tabs

######Earthquake
    Display Name: Earthquake
    Order: 0
    Likely Scenario Title:
    Likely Scenario Text:

######Flood
    Display Name: Flood
    Order: 1
    Likely Scenario Title:
    Likely Scenario Text:

######Landslide:
    Display Name: Landslide
    Order: 2
    Likely Scenario Title:
    Likely Scenario Text:

######Fire
    Display Name: Wildfire
    Order: 3
    Likely Scenario Title:
    Likely Scenario Text:

######Volcano
    Display Name: Volcano
    Order: 4
    Likely Scenario Title:
    Likely Scenario Text:

### Section orders

###### Snugget Section
  What to expect: 0
  How to prepare: 1
  In Recent History: 2

###### Snugget Subsection
Note that these may appear in different sections or be mutually exclusive, which is why some of them have the same order.

  In Your Lifetime: 0
  Cascadia Quake: 1
  What's the Worst: 2
  Erosion Risk: 3
  If the dams failed: 3
  Tsunami Zone: 3
  Liquefaction: 4
  Unstable Structures:54
  Warning Signs: 6
  Before: 7
  During: 8
  After: 9
  Local Resources: 10
  What's Happened?: 11
  Historical Images: 12

### Important links

### Supply kit

###### days
  3
###### text
Supply kit text goes here

### Location Information

###### Area Name
King County

###### Community Leaders
Community leaders (FEMA?) contact information goes ehre.

### Settings

###### About Text
This site is a collaboration of HazardReady, the University of Montana, King County, and the City of Seattle.

###### Site title
Seattle and King County Ready

###### URL
https://hazardready.org/seattle

###### Site description
A disaster preparedness website

###### Intro Text
A natural disaster could strike your area at any time. Find out about where you live, work, or play in King County, WA.

###### Who Made This
`This is based on <a href="http://www.opb.org/news/widget/aftershock-find-your-cascadia-earthquake-story/" target="_blank">Aftershock</a>, an earthquake preparedness application for Oregon residents. Carson MacPherson-Krutsky and <a href="https://hs.umt.edu/geosciences/faculty/bendick/" target="_blank">Dr. Rebecca Bendick</a>, a graduate student and her advisor at the Unversity of Montana, had the idea to expand it for other locales and types of disasters. <a href="https://github.com/nein09" target="_blank">Melinda Minch</a> and <a href="https://github.com/eldang" target="_blank">Eldan Goldenberg</a> adapted it for that purpose. Source for a general-purpose version of this site is available on <a href="https://github.com/missoula-ready/disaster-preparedness" target="_blank">Github</a>.
<br/>
Content and data are supported by several entities including the <a href="http://www.umt.edu/" alt="logo" target="_blank">University of Montana</a>, <a href="http://www.kingcounty.gov/" alt="logo" target="_blank">King County</a>, and the <a href="http://www.seattle.gov/" alt="logo" target="_blank">City of Seattle</a>.
<br/>
<img class="who-made-this-logo umt-logo" src="static/img/umt_logo.png">
<img class="who-made-this-logo county-logo" src="static/img/kc_logo_bw.gif">
<img class="who-made-this-logo city-logo" src="static/img/seattle_logo_bw.png">`

###### Data Download
https://github.com/hazard-ready/seattle-ready/blob/master/disasterinfosite/data.zip

###### Past Events Photos
Upload photos to show in a photo gallery in the search results, under Past Events. Make sure that the heading you enter here matches the heading that the photos will appear under.

###### Data Overview Images
In the box at the bottom of every page, there's a section called 'Quick Data Overview'. That's where these will show up, as links that open in a new tab or window. The link_text field is what the link says, like 'Earthquakes: Distance from a Fault', and you can upload the appropriate image here.

### Deploying to the web via Apache
There are directories called 'photos' and 'data' in disasterinfosite/img. This is where images go when you upload them via Django Admin, under 'Photos of Past Events' and 'Data Overview Images'. In order for that upload to work, you need to change the owner (chown) those directories to whatever user Apache is running as (www-data, perhaps).

