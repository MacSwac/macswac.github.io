{% assign countries = site.travel | group_by: "country" %}

{% for country in countries %}
  <tr>
    <td>
      <a href="/travel/{{ country.name | slugify }}/">
        {{ country.name }}
      </a>
    </td>
  </tr>
{% endfor %}
