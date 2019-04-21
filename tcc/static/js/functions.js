




function teste(lista){

    		document.addEventListener('DOMContentLoaded', function() {

      		/*lista = '{%  for c in consultas %} {{c}}, {% endfor %}';

    		var listares = lista.split(",");*/

    			
	        var calendarEl = document.getElementById('calendar');
	        var elements = []

	        for (var l in listares){
	        	console.log(l);
	        	console.log(listares[l]);
	        	var elem = {
	        		title  : 'Consulta',
				    start  : listares[l]
	        	};
	        	elements.push(elem);

	        }
	        alert("TESTE: ", lista);
	       
	        var calendar = new FullCalendar.Calendar(calendarEl, {

	          	plugins: [ 'dayGrid', 'timeGrid', 'list', 'interaction', 'googleCalendar', 'timeline' ],

	          	defaultView: 'dayGridMonth',
	  			selectable: true,
	  			editable: true,

	  			timeZone: 'local',
				eventLimit: true, 
	    		events: elements,
				 
			    dateClick: function(info) {
				    alert('Data: ' + info.dateStr);
				    alert('Resource ID: ' + info.resource.id);
				    
				}
	        });
	        calendar.render();
	      });
    	}

    	
      	

   
	    