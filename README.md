
<a name="readme-top"></a>

<!-- ABOUT THE PROJECT -->
## About The Project

Using the [yad2 website](https://www.yad2.co.il/), scrape and collect information about apartments in your area.  
*currently => Haifa, Israel

<!-- GETTING STARTED -->
## Getting Started

1. edit the "config.json" file with the parameters of the search  
  using strings with format "<minimum_value>-<maximum_value>"  
  for Any value enter "-1"  
  Exemple:  
    ```json
    {
      "rooms": "2--1",
      "price": "-1-2600",
      "floor": "-1--1",
    }
    ```  
2. using int format.
  to include the parameter in search = 1  
  to exclude the parameter in search = 0  
    Exemple:  
    ```json
    {
      "parking": 0, 
      "elevator": 1
    }
    ``` 
3. Install dependencies
   ```sh
   pip install -r requirements.txt
   ```
4. Run in your terminal
   ```sh
   python scrape.py
   ```

<!-- USAGE EXAMPLES -->
## Usage

After the program finish running, an output file "apartment_listings" will be created with all the apartments found.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ROADMAP -->
## Roadmap

- [x] Scarpe single page of the webside
- [x] Scrape all possible pages of the search results. Save in the output file
- [ ] Scrape each item for additional details and images
- [ ] Add support for other file formats. (currently only works with .csv)

See the [open issues](https://github.com/Leo-project-A/Apartment_hunting/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTACT -->
## Contact

Leonid Sobol - leonis313@gmail.com

Project Link: [https://github.com/Leo-project-A/Apartment_hunting](https://github.com/Leo-project-A/Apartment_hunting)

<p align="right">(<a href="#readme-top">back to top</a>)</p>