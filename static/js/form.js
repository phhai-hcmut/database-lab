// https://stackoverflow.com/a/669982
function addForm(selector, type) {
	var newElement = $(selector).clone(true)
	// Update the management_form field
	var total = $('#id_${type}-TOTAL_FORMS').val()
	// Increase index number in new form
	newElement.find(':input').each(function() {
		var name = $(this).attr('name').replace('-' + (total - 1) + '-', '-' + total + '-')
		var id = 'id_' + name
		$(this).attr({
			'name': name,
			'id': id
		}).val('').removeAttr('checked')
	})
	newElement.find('label').each(function() {
		var newFor = $(this).attr('for').replace('-' + (total - 1) + '-', '-' + total + '-')
		$(this).attr('for', newFor)
	})
	var trackNumSelector = '#id_' + type + '-' + total + '-track_number'
	var lastTrackNumber = newElement.find(trackNumSelector).val()
	console.log('track num is ' + newElement.find(trackNumSelector))
	newElement.find(trackNumSelector).attr('value', lastTrackNumber + 1)
	total++
	$('#id_${type}-TOTAL_FORMS').val(total)
	$(selector).after(newElement)
}
