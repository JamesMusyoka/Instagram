{% autoescape off %}
Hi {{ user.username }},
Please click on the link to confirm your registration,
http://{{ domain }}{% url 'activate' uidb64=uid token=token %}
{% endautoescape %}