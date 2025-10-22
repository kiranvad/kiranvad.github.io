// Citation Histogram Visualization
// Uses Chart.js to create an interactive citation histogram

document.addEventListener('DOMContentLoaded', function() {
    // Get citation data from the data attributes
    const citationData = JSON.parse(document.getElementById('citation-chart').getAttribute('data-citations'));
    
    // Extract years and citation counts
    const years = Object.keys(citationData).sort();
    const citations = years.map(year => citationData[year]);
    
    // Create the chart
    const ctx = document.getElementById('citation-chart').getContext('2d');
    const chart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: years,
            datasets: [{
                label: 'Citations',
                data: citations,
                backgroundColor: 'rgba(54, 162, 235, 0.8)',
                borderColor: 'rgba(54, 162, 235, 1)',
                borderWidth: 1,
                borderRadius: 4,
                borderSkipped: false,
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                title: {
                    display: true,
                    text: 'Citations by Year',
                    font: {
                        size: 16,
                        weight: 'bold'
                    }
                },
                legend: {
                    display: false
                }
            },
            scales: {
                y: {
                    beginAtZero: true,
                    ticks: {
                        stepSize: 1
                    },
                    title: {
                        display: true,
                        text: 'Number of Citations'
                    }
                },
                x: {
                    title: {
                        display: true,
                        text: 'Year'
                    }
                }
            },
            interaction: {
                intersect: false,
                mode: 'index'
            },
            animation: {
                duration: 1000,
                easing: 'easeInOutQuart'
            }
        }
    });
});
