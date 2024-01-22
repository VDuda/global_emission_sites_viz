# Global Climate Visualized 

Demo Publicly Accessible: [https://global-emissions.onrender.com](https://global-emissions.onrender.com)




## Description

Climate TRACE is a non-profit alliance that was established in 2020. They utilize satellite imagery, specialized datasets, and various other resources to provide comprehensive estimates of greenhouse gas emissions. Their analysis specifically focuses on over 70,000 individual locations that are considered significant contributors to emissions in sectors such as power generation, oil and gas extraction and refining, shipping, aviation, mining, waste management, agriculture, road transportation, as well as the production of steel, cement, and aluminum.

### Diagram explained

Divided by Sector, End Use, Gas

### Running app 
```
# Direct access to app for QA
python sankey_app/src/app.py
```

```
# Webserver
gunicorn --timeout 600 --chdir sankey_app/src app:server
```

Interactive demo should be publicly accessible on render.
```
https://global-emissions.onrender.com
``` 


## Generating Submission 

```
python submission.py
```

## Data Source / Links / Resources

- https://climatetrace.org/downloads 
- https://climatetrace.org/inventory 
- https://www.nytimes.com/2022/11/09/climate/climate-change-emissions-satellites.html 
- https://www.drivendata.org/competitions/256/pale-blue-dot/page/802/ 
- https://plotly.com/python/sankey-diagram/
