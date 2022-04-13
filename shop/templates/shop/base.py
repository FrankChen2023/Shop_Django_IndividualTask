<html>
    <head><title>Shop base</title></head>
    <body>
        <p>
        <a href = "{% url 'shop:index' %}">Home</a>
        {% if user.is_staff %}
        <a href = "{% url 'shop:product_add' %}">Add Product</a> 
        <a href = "{% url 'shop:product_list' %}">Check List</a> 
        {% elif user.is_authenticated %}
        <a href = "{% url 'shop:basket' %}">Basket</a>
        <a href = "{% url 'shop:payment' %}">Payment</a> 
        {% else %}
        <a href = "{% url 'shop:logout' %}">Log Out</a> 
        </p> 
        {% block content %}
        {% endblock %}
    </body>
</html>