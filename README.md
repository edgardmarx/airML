# airML

This package is created to distribute KBox, which allow users to share and dereference ML models.

### You can use airML in the command line

* Download the library [here] (https://pypi.org/project/airML/)

* Type the following:
```
airML <command> [option]
Where [command] is:
   * -createIndex <directory>    - Create an index with the files in a given directory.
                                 ps: the directory might contain only RDF compatible file formats.
   * -serialize <directory>      - Serialize the content of a directory to be served in a KNS system.
   * -sparql <query> (-kb <KB> | -server <URL>) [-install] [-json]       - Query a given KB (e.g. -sparql "Select ..." -kb "KB1,KB2")
                                                 - ps: use -install in case you want to enable the auto-dereference.
   * -server [-port <port> (default 8080)] [-subDomain <subDomain> (default kbox)] -kb <KB> [-install]   - Start an SPARQL enpoint in the given subDomain containing the given KB.
   * -list       - List all available knowledge base.
   * -list -kns  - List all availables KNS services.
   * -install <URL>      - Install a given resource.
   * -install -kns <kns-URL>     - Install a given KNS service.
   * -install -kb <kb-URL>       - Install a given knowledge base using the available KNS services to resolve it.
   * -install -kb <kb-URL> -format <format>      - Install a given knowledge base using the available KNS services to resolve it.
   * -install -kb <kb-URL> -format <format> -version <version>   - Install a given knowledge base using the available KNS services to resolve it.
   * -install -kb <kb-URL> -index <indexFile>    - Install a given index in a given knowledge base URL.
   * -install -kb <kb-URL> -kns <kns-URL>        - Install a knowledge base from a a given KNS service.
   * -install -kb <kb-URL> -kns <kns-URL> -format <format> -version <version> - Install a knowledge base from a a given KNS service with the specific format and version.
   * -remove -kns <kns-URL>      - Remove a given KNS service.
   * -info <kb-URL>      - Gives the information about a specific KB.
   * -info <kb-URL> -format <format>     - Gives the information about a specific KB.
   * -info <kb-URL> -format <format> -version <version>  - Gives the information about a specific KB.
   * -locate <URL>       - returns the local address of the given resource.
   * -locate -kb <kb-URL>        - returns the local address of the given KB.
   * -locate -kb <kb-URL> -format <format>       - returns the local address of the given KB.
   * -locate -kb <kb-URL> -format <format> -version <version>    - returns the local address of the given KB.
   * -search <kb-URL-pattern>    - Search for all kb-URL containing a given pattern.
   * -search <kb-URL-pattern> -format <format>   - Search for all kb-URL containing a given pattern.
   * -search <kb-URL-pattern> -format <format> -version <version>        - Search for all kb-URL containing a given pattern.
   * -r-dir      - Show the path to the resource folder.
   * -r-dir <resourceDir>        - Change the path of the resource folder.
   * -version    - display KBox version.
```

* See the source for this project [here] (https://github.com/AKSW/airML)
* Find the KBox source cord [here] (https://github.com/AKSW/KBox)
