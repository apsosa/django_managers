## Django Models Manager vs QuerySets


Before we move forward, let me give you a quick explanation about the ORM and its patterns.

- Model — It implements the Active Record pattern. In this pattern, the Object wraps a row in a database table (or view). The object carries both data and behavior and it is, in most cases, persisted in data storage through Model Managers. One of the responsibilities the model class has within the ORM design is to carry the metadata used to map the result of the queries into Python objects that is defined by Fields, as well as the metadata for the entity that lives on a data storage such as the table name and primary key. The query set uses this map to perform its operations and return an instance (or instances) of the model with the data perfectly mapped to the object attributes.

- Fields — A field is a representation of a column in your data storage. It contains all the storage constraints such as “null”, “length”, “type”, and “unique”.
Fields implement the ValueObject pattern, therefore, they have no meaning by itself. However, there is a type of field that implements a different pattern, the relational fields.
Relational fields are ForeignKey field, OneToOne field, and ManyToMany field. Those implement the ForeignKey mapping, Dependent mapping, and Association table mapping patterns respectively. They are responsible for defining the Metadata needed for the Data mapping that will be done by Query Sets.

- Manager — According to Django documentation, a manager is an interface through which database query operations are provided to models.Also:
  Managers are accessible only via model classes, rather than from model instances, to enforce a separation between “table-level” operations and “record-level” operations.The Manager is the main source of QuerySets for a model. For example, Blog.objects.all() returns a QuerySet that contains all Blog objects in the database.

It implements partially the Table Gateway pattern. However, Managers delegate performing the queries to Query Sets.
I always see Managers more like a “Facade” for the complexity of the operations on your data storage. Although, another approach I like is to use them as Repositories in some projects (I will talk more about that in another post).
Whenever you need to perform a query, insert data, or manipulate existing data, the manager can be powerful for simplifying this process for external usage on your application.

- Query Sets — Query sets are the final frontier between your domain and your data storage. They implement the Query Object pattern (named by Martin Fowler). Query sets allow you to build queries with python objects and use different backends to convert those queries to the real SQL query that will be performed in a data storage.
Whenever you need to customize the way the SQL query will be built or its response, Query Sets are the right place to do it.
Query sets perform queries using the pattern known as Lazy Load, which means that queries are performed only when the application actually requires the result. You can play with a query set as much as you want before it really gets evaluated.

- Backends — They perform the mapping from Query objects to SQL queries for a particular data storage. It is very powerful if you consider that by implementing this interface, you can talk to pretty much every data storage, from SQL to No-SQL. I’ve rarely seen customizations at this level.


So here is an overview of the components described above.


![Overview of the components described above](/manager_view.png "Components")


I guess it already gives you a glance of the role of the Manager and a Query Set. However, one of the most frequent questions I get on projects is whether you should add custom queries on one or the other.

Like I mentioned earlier here, the manager can be interpreted as a “Facade” that simplifies the complexity of operations you want to perform on your data storage. Every time I have a query to perform with known parameters, I add methods to abstract the creation of the Query set. I also work really hard to keep my queries very simple and avoid “leaking” the internals of my models.

But from time to time you have really complex queries in your project. Queries that involve annotations or even complex filters that should be known only by a specific domain.














#### ***Wrapping up***
Put in your Managers methods that make sense for the external world with meaningful parameters. Put in your query sets methods that change the structure of the response of your query, or perform any kind of operations such as aggregations and annotations.

To be clear, simple queries — Managers, complex queries — QuerySets. However, never access query sets directly, making your manager as the Facade layer will prevent you from having multiple queries for the same purpose all over the place. 

Thus, there's just one source of truth for the external world, the manager. It is way easier to maintain when your application scales. Trust me!




##### References:

- This repository it's complete base on the [article](https://jairvercosa.medium.com/manger-vs-query-sets-in-django-e9af7ed744e0) made for Jair Vercosa 