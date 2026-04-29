frappe.pages['manchipustakam'].on_page_load = function(wrapper) {

	var page = frappe.ui.make_app_page({
		parent: wrapper,
		title: 'Manchi Pustakam Dashboard',
		single_column: true
	});

	$(page.body).html(`
		<div class="mp-container">

			<div class="mp-row">

				<div class="mp-card card-books">
					<div class="mp-icon"></div>
					<h4>Total Books</h4>
					<h2 id="total_books">0</h2>
				</div>

				<div class="mp-card card-groups">
					<div class="mp-icon"></div>
					<h4>Age Groups</h4>
					<h2 id="total_age_groups">0</h2>
				</div>

				<div class="mp-card card-subject">
					<div class="mp-icon"></div>
					<h4>Subjects</h4>
					<h2 id="total_subjects">0</h2>
				</div>

				<div class="mp-card card-publisher">
					<div class="mp-icon"></div>
					<h4>Publishers</h4>
					<h2 id="total_publishers">0</h2>
				</div>

				<div class="mp-card card-author">
					<div class="mp-icon"></div>
					<h4>Authors</h4>
					<h2 id="total_authors">0</h2>
				</div>

			</div>

			<div class="mp-chart-container full">
				<h4>Age Group Wise Books</h4>
				<div id="chart_age"></div>
			</div>

			<div class="mp-chart-grid">

				<div class="mp-chart-container">
					<h4>Subject Wise Books</h4>
					<div class="chart-flex">
						<div id="legend_subject" class="legend"></div>
						<div id="chart_subject" class="chart-box"></div>
					</div>
				</div>

				<div class="mp-chart-container">
					<h4>Publisher Wise Books</h4>
					<div class="chart-flex">
						<div id="legend_publisher" class="legend"></div>
						<div id="chart_publisher" class="chart-box"></div>
					</div>
				</div>

			</div>

			<div class="mp-chart-container full">
				<h4>Author Wise Books</h4>
				<div id="chart_author"></div>
			</div>

		</div>

		<style>
		.mp-container { padding:20px; background:#f5f7ff; }

		.mp-row {
			display:flex;
			gap:15px;
			margin-bottom:15px;
			flex-wrap:wrap;
		}

		.mp-card {
			flex:1;
			min-width:160px;
			padding:16px;
			border-radius:14px;
			text-align:center;
			background:#fff;
			box-shadow:0 4px 12px rgba(0,0,0,0.04);
		}

		.mp-icon { font-size:22px; margin-bottom:6px; }

		.card-books { background:#f0f9ff; }
		.card-groups { background:#fff7ed; }
		.card-subject { background:#f0fdf4; }
		.card-publisher { background:#fef3c7; }
		.card-author { background:#fdf2f8; }

		.mp-chart-container {
			background:#fff;
			padding:20px;
			border-radius:16px;
			box-shadow:0 4px 14px rgba(0,0,0,0.05);
			margin-bottom:20px;
		}

		.full { width:100%; }

		.mp-chart-grid {
			display:grid;
			grid-template-columns: repeat(2, 1fr);
			gap:20px;
		}

		.chart-flex {
			display:flex;
			gap:20px;
			align-items:flex-start;
		}

		.legend {
			max-height:250px;
			overflow-y:auto;
			min-width:180px;
			font-size:12px;
		}

		.chart-box {
			flex:1;
			min-width:250px;
		}

		.legend-item {
			display:flex;
			align-items:center;
			margin-bottom:6px;
		}

		.legend-color {
			width:10px;
			height:10px;
			border-radius:2px;
			margin-right:8px;
		}

		#chart_subject svg g.chart-label,
		#chart_subject svg g.tick,
		#chart_subject svg text,
		#chart_publisher svg g.chart-label,
		#chart_publisher svg g.tick,
		#chart_publisher svg text {
			display:none !important;
		}
		</style>
	`);

	load_all_data();
};

let colors = [
	"#bfdbfe","#fde68a","#bbf7d0","#fbcfe8",
	"#ddd6fe","#bae6fd","#fef3c7","#fecdd3",
	"#d1fae5","#e0f2fe","#ffedd5","#cffafe"
];

function load_all_data() {

	frappe.db.count("Item").then(count => {
		$("#total_books").text(count || 0);
	});

	frappe.call({
		method: "frappe.client.get_list",
		args: {
			doctype: "Item",
			fields: ["custom_age_group","item_group","brand","custom_author"],
			limit_page_length: 1000
		},
		callback: function(r) {

			let data = r.message || [];

			set_card_counts(data);

			render_group_chart(data, "custom_age_group", "#chart_age", null, "bar", "total_age_groups");
			render_group_chart(data, "item_group", "#chart_subject", "#legend_subject", "pie");
			render_group_chart(data, "brand", "#chart_publisher", "#legend_publisher", "donut");
			render_group_chart(data, "custom_author", "#chart_author", null, "bar");
		}
	});
}

function set_card_counts(data) {

	let subjects = new Set();
	let publishers = new Set();
	let authors = new Set();

	data.forEach(d => {
		if (d.item_group) subjects.add(d.item_group);
		if (d.brand) publishers.add(d.brand);
		if (d.custom_author) authors.add(d.custom_author);
	});

	$("#total_subjects").text(subjects.size);
	$("#total_publishers").text(publishers.size);
	$("#total_authors").text(authors.size);
}

function render_group_chart(data, field, chart_id, legend_id, type, count_id=null) {

	let unique = new Set();
	let groupCount = {};

	data.forEach(row => {
		let val = row[field] || "Unknown";
		unique.add(val);
		groupCount[val] = (groupCount[val] || 0) + 1;
	});

	if (count_id) {
		$("#" + count_id).text(unique.size);
	}

	let labels = Object.keys(groupCount);
	let values = Object.values(groupCount);

	let sorted = labels.map((l, i) => ({ label: l, value: values[i] }))
		.sort((a, b) => b.value - a.value)
		.slice(0, 10);

	labels = sorted.map(d => d.label);
	values = sorted.map(d => d.value);

	if (legend_id) {
		render_legend(labels, values, legend_id);
	}

	render_chart(labels, values, chart_id, type);
}

function render_legend(labels, values, legend_id) {

	let html = "";

	labels.forEach((label, i) => {
		html += `
			<div class="legend-item">
				<div class="legend-color" style="background:${colors[i % colors.length]}"></div>
				<div>${label} (${values[i]})</div>
			</div>
		`;
	});

	$(legend_id).html(html);
}

function render_chart(labels, values, container, type) {

	frappe.require("assets/frappe/js/lib/frappe-charts.min.js", function () {

		$(container).empty();

		if (type === "bar") {

			let datasets = labels.map((label, i) => {
				let arr = new Array(labels.length).fill(0);
				arr[i] = values[i];
				return {
					name: label,
					values: arr,
					chartType: "bar",
					color: colors[i % colors.length]
				};
			});

			new frappe.Chart(container, {
				data: { labels: labels, datasets: datasets },
				type: "bar",
				height: 320,
				barOptions: { spaceRatio: 0.2 }
			});

			setTimeout(() => {

				let rects = document.querySelectorAll(container + " svg rect");
				let bars = [];

				rects.forEach(r => {
					let h = parseFloat(r.getAttribute("height"));
					if (h > 0) bars.push(r);
				});

				bars = bars.slice(-labels.length);

				bars.forEach((bar, i) => {

					let x = parseFloat(bar.getAttribute("x")) + parseFloat(bar.getAttribute("width")) / 2;
					let y = parseFloat(bar.getAttribute("y")) - 6;

					let text = document.createElementNS("http://www.w3.org/2000/svg", "text");

					text.setAttribute("x", x);
					text.setAttribute("y", y);
					text.setAttribute("text-anchor", "middle");
					text.setAttribute("font-size", "11");
					text.setAttribute("font-weight", "600");
					text.setAttribute("fill", "#333");

					text.textContent = values[i];

					bar.parentNode.appendChild(text);
				});

			}, 400);

		} else {

			new frappe.Chart(container, {
				data: {
					labels: labels,
					datasets: [{ values: values }]
				},
				type: type,
				height: 280,
				colors: colors,
				tooltipOptions: {
					formatTooltipY: (d) => d
				}
			});

			setTimeout(() => {

				$(container).find("g.chart-label").remove();
				$(container).find("g.tick").remove();
				$(container).find("g.legend").remove();
				$(container).find("circle").remove();

			}, 300);
		}
	});
}