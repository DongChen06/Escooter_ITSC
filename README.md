# Escooter_ITSC
This repo contains the codes for our submission to IEEE ITSC'24: **Impact of Different Infrastructures and Traffic Scenarios on Behavioral and Physiological Responses of E-scooter Users**

## Installation
- create a python virtual environment: `conda create -n scooter python=3.8 -y`
- active the virtul environment: `conda activate scooter`
- install the requirements: `pip install -r requirements.txt`

## Gaze Density Maps
1. propocess the gaze data via: `python generate_whole_excel_facilities.py`
2. plot the gaze density map via: `python plot_gaze_density_facilities.py`

Fixation Metrics:
<table>
<tr>
  <td>
    <p align="center">
      <img src="Gaze_entropy_facilities/fixation_metrics.png" alt="First Image" width="100%" />
      <br>
      <em>Fixation metrics</em>
    </p>
  </td>
  <td>
    <p align="center">
      <img src="Gaze_entropy_facilities/prc_metric.png" alt="Second Image" width="100%" />
      <br>
      <em>PRC metric</em>
    </p>
  </td>
</tr>
</table>

Entropy Metrics:
<table>
<tr>
  <td>
    <p align="center">
      <img src="Gaze_entropy_facilities/gaze_entropy_metrics.png" alt="First Image" width="100%" />
      <br>
      <em>Gaze entropy metrics</em>
    </p>
  </td>
  <td>
    <p align="center">
      <img src="Gaze_entropy_facilities/gaze_variability_metrics.png" alt="Second Image" width="100%" />
      <br>
      <em>Gaze Variability metric</em>
    </p>
  </td>
</tr>
</table>



## Citation
Coming soon...