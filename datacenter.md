# Data Center Report by Josh Goodman sp20-516-220

## Sacramento Data Center Campus

### Overview

The Sacramento Data Center [@primedatacenters] is a newly constructed (2019)  data center that is owned
by Prime Data Centers Inc [@mcclellanparkdatacenter].  It is located in McClellan Park [@mcclellanpark]
outside of Sacramento, CA.

### Building One Specifications

* 68,853 square ft
* 40,000 usable floor space
* 8 MW power

[@primedatacenters]

### Power source

Power for the Prime Data Center Campus is supplied by Sacramento Municipal Utility District,
which utilizes natural gas, hydroelectric, and renewable energy sources to generate its
electricity.

* 54% Natural Gas
* 26% Large Hydroelectric
* 20% Eligible Renewable

Power data sourced from Power Content Label [@smudpcl].

### Cost of power

Using data from OpenEI [@openeiurd] it is estimated
that the average cost of electricity for this facility will be $0.104 per kWh.

### Future growth

The site currently has only one building, but has 38 acres and 100 MW of potential growth capacity.

## Power Sources

### Other Renewable Sources

Data Centers get their power from a variety of renewable data sources.  Unfortunately, most of these sources 
are problematic in terms of the alignment of the supply and demand curves.  For example, solar power generation peaks in the middle
of the day and declines into the evening, whereas demand for power is generally low in the middle of the day and 
peaks in the evening.  To even this out engineers have devised systems called pumped storage
hydropower.

#### Pumped Storage Hydropower 

In a pumped storage hydropower system
two or more bodies of water are set at different elevations [@doepsh].  In a closed loop system you have two or more
bodies of water that have no connection to an outside body of water.  In an open loop system
you would have two or more bodies of waters with one of them having a connection to an outside body of water.
For example, an elevated and isolated reservoir along with a damned river.

When power in the grid is in surplus, the excess power is used to power water pumps that take
water from the lower body of water and move it to the upper body of water.
Then when additional power is required by the grid, the flow of water
is reversed and used to turn turbine generators, which in turn generate power that feeds back into the grid.

Thus, these systems act as giant batteries, storing excess energy as potential energy by
using the water pumped to a higher elevation.  This can then be released on demand in order to 
better align supply/demand power requirements.

##### Bath County Pumped Storage Station

One such pumped storage hydropower station is the Bath County Pumped Storage station [@bathcountypsh].
This station is the largest of its kind in the United States and feeds power into the PJM Interconnection [@pjmhome], which includes
all of the Virginia area.

##### Harrisonburg, VA Data Center

Harrisonburg, VA, which lies inside the PJM Interconnection zone has a data center that relies on power
from this station among others [@dbtcyberintegrationcenter].

## Renewable Energy Efforts in Hawaii

Hawaii has made a bold commitment to generate 100% of their energy from renewable sources by 2045 [@hawaiienergy].
They hope to do this by taking advantage of their natural surroundings and a variety of technologies.  These technologies
include:

* Biofuel
* Biomass
* Geothermal
* Hydroelectric
* Ocean (cooling and wave energy)
* Solar
* Waste-to-Energy
* Wind

While they are uniquely positioned to do so, given their weather and unique
geography (volcanic activity, ocean, sun, wind, etc.), they face an uphill
battle given their current sources of electricity.

As of 2018, their current sources of electricity include:

| Source              | Percent |
| ------------------- | ------- | 
| Petroleum  | 61.3  |
| Coal | 11.9 |
| Small-scale Solar | 9.3 |
| Wind | 4.9 |
| Other | 4.0 |
| Geothermal | 2.9 |
| Biomass | 2.8 |
| Utility-scale Solar |1.9 |
| Hydroelectric | 0.9 |

* [@hawaiienergy]
* [@hawaiienergyprojects]

## Data Center Outages

On December 27, 2018, CenturyLink, an internet service provider, started experiencing failures across its
nationwide fiber network.  This outage lasted for 37 hours.  The root cause was found to be the failure
of a single device in one of their data centers that then caused a cascade of errors due to network 
configuration errors.  According to the FCC report
on the failure [@fcccenturylink], the estimated number of users affected by this failure was 22 million across 39 states.

Services impacted spanned across many different services including:

* 911 phone services
* Long distance phone calls
* ATM transfers
* State governmental entities
* Other Providers (Verizon Wireless, Comcast, AT&T)
 

## References
