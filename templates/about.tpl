{% extends "layout.tpl" %}

{% block content %}
<ul>
	<div class="interest-block">
		<img src="{{ url_for('static', filename="img/about-bansko.jpg") }}">
		<img src="{{ url_for('static', filename="img/about-athens.jpg") }}" />
		<img src="{{ url_for('static', filename="img/about-photo-v.jpg") }}"/>
		<img src="{{ url_for('static', filename="img/about-photo-v-2.jpg") }} width="100px" />	
		<img src="{{ url_for('static', filename="img/about-gym.jpg") }}" />	
	</div>
</ul>
{% endblock %}
