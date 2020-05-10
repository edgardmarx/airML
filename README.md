# airML

This package is created to distribute KBox, which allow users to share and dereference ML models.

### You can use airML in the command line

* Download the library [here] (https://pypi.org/project/airML/)

* Type the following:
```
airML <command> [option]
Where [command] is:
   * -list       - List all available models.
   * -list -kns  - List all availables KNS services.
   * -install -kns <kns-URL>     - Install a given KNS service.
   * -install -model <modelID>       - Install a given model using the available KNS services to resolve it.
   * -install -model <modelID> [-kns <kns-URL>] [-format <format>] [-version <version>] - Install a model from a a given KNS service with the specific format and version.
   * -remove -kns <kns-URL>      - Remove a given KNS service.
   * -info <modelID> [-format <format>] [-version <version>]  - Gives the information about a specific model.
   * -locate <modelID>       - returns the local address of the given model.
   * -locate -model <modelID> [-format <format>] [-version <version>]  - returns the local address of the given KB.
   * -search <pattern> [-format <format>] [-version <version>]        - Search for all models containing a given pattern.
   * -models      - Show the path to the model folder.
   * -models <modelDir>        - Change the path of the model folder.
   * -version    - display airML version.
```

* See the source for this project [here] (https://github.com/AKSW/airML)
