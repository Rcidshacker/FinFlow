/**
 * Recommendations Dashboard JavaScript
 * Tab switching and Chart.js integration
 */

// Chart instances (global for reference)
let stocksPieChart = null;
let fnoScatterChart = null;

document.addEventListener('DOMContentLoaded', function () {
    // Initialize tab switching
    initTabs();

    // Initialize charts (if Chart.js is loaded)
    if (typeof Chart !== 'undefined') {
        initCharts();
    }

    // Refresh button
    const refreshBtn = document.querySelector('.refresh-btn');
    if (refreshBtn) {
        refreshBtn.addEventListener('click', refreshRecommendations);
    }
});

// Tab switching logic
function initTabs() {
    const tabButtons = document.querySelectorAll('.tab-btn');
    const tabContents = document.querySelectorAll('.tab-content');

    tabButtons.forEach(btn => {
        btn.addEventListener('click', function () {
            const tabName = this.dataset.tab;

            // Update active button
            tabButtons.forEach(b => b.classList.remove('active'));
            this.classList.add('active');

            // Update active content
            tabContents.forEach(c => c.classList.remove('active'));
            const targetContent = document.getElementById(`${tabName}-tab`);
            if (targetContent) {
                targetContent.classList.add('active');
            }

            // Trigger chart resize for proper rendering
            setTimeout(() => {
                if (tabName === 'stocks' && stocksPieChart) {
                    stocksPieChart.resize();
                } else if (tabName === 'fno' && fnoScatterChart) {
                    fnoScatterChart.resize();
                }
            }, 100);
        });
    });
}

// Initialize charts
function initCharts() {
    initStocksPieChart();
    initFNOScatterChart();
}

// Stocks Pie Chart
function initStocksPieChart() {
    const canvas = document.getElementById('stocksPieChart');
    if (!canvas) return;

    const ctx = canvas.getContext('2d');

    // Get data from script tag or data attributes
    const labels = window.stockLabels || [];
    const data = window.stockData || [];

    if (labels.length === 0) return;

    // Color palette
    const colors = [
        'rgba(58, 134, 255, 0.8)',
        'rgba(139, 92, 246, 0.8)',
        'rgba(16, 185, 129, 0.8)',
        'rgba(245, 158, 11, 0.8)',
        'rgba(239, 68, 68, 0.8)',
        'rgba(236, 72, 153, 0.8)',
        'rgba(99, 102, 241, 0.8)',
        'rgba(20, 184, 166, 0.8)'
    ];

    stocksPieChart = new Chart(ctx, {
        type: 'doughnut',
        data: {
            labels: labels,
            datasets: [{
                data: data,
                backgroundColor: colors.slice(0, data.length),
                borderColor: 'rgba(255, 255, 255, 0.1)',
                borderWidth: 2,
                hoverBorderWidth: 3,
                hoverBorderColor: 'rgba(255, 255, 255, 0.5)'
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            cutout: '60%',
            plugins: {
                legend: {
                    display: true,
                    position: 'right',
                    labels: {
                        color: '#B8B8B8',
                        padding: 15,
                        usePointStyle: true,
                        pointStyle: 'circle',
                        font: {
                            family: "'Inter', sans-serif",
                            size: 12
                        }
                    }
                },
                tooltip: {
                    backgroundColor: 'rgba(31, 31, 31, 0.95)',
                    titleColor: '#fff',
                    bodyColor: '#fff',
                    borderColor: 'rgba(58, 134, 255, 0.5)',
                    borderWidth: 1,
                    padding: 12,
                    cornerRadius: 8,
                    displayColors: true,
                    callbacks: {
                        label: function (context) {
                            const value = context.parsed;
                            return `${context.label}: ₹${value.toLocaleString('en-IN')}`;
                        }
                    }
                }
            },
            animation: {
                animateRotate: true,
                animateScale: true
            }
        }
    });

    // Generate custom legend
    generateChartLegend(labels, colors);
}

// F&O Scatter Chart
function initFNOScatterChart() {
    const canvas = document.getElementById('fnoScatterChart');
    if (!canvas) return;

    const ctx = canvas.getContext('2d');

    // Get data from window variables
    const callData = window.callData || [];
    const putData = window.putData || [];

    if (callData.length === 0 && putData.length === 0) return;

    fnoScatterChart = new Chart(ctx, {
        type: 'scatter',
        data: {
            datasets: [{
                label: 'Call Options',
                data: callData,
                backgroundColor: 'rgba(16, 185, 129, 0.6)',
                borderColor: 'rgba(16, 185, 129, 1)',
                pointRadius: 10,
                pointHoverRadius: 14,
                pointBorderWidth: 2
            }, {
                label: 'Put Options',
                data: putData,
                backgroundColor: 'rgba(239, 68, 68, 0.6)',
                borderColor: 'rgba(239, 68, 68, 1)',
                pointRadius: 10,
                pointHoverRadius: 14,
                pointBorderWidth: 2
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            scales: {
                x: {
                    title: {
                        display: true,
                        text: 'Position Number',
                        color: '#B8B8B8',
                        font: {
                            family: "'Inter', sans-serif",
                            size: 12
                        }
                    },
                    grid: {
                        color: 'rgba(255, 255, 255, 0.05)'
                    },
                    ticks: {
                        color: '#B8B8B8'
                    }
                },
                y: {
                    title: {
                        display: true,
                        text: 'Potential Profit (₹)',
                        color: '#B8B8B8',
                        font: {
                            family: "'Inter', sans-serif",
                            size: 12
                        }
                    },
                    grid: {
                        color: 'rgba(255, 255, 255, 0.05)'
                    },
                    ticks: {
                        color: '#B8B8B8',
                        callback: function (value) {
                            return '₹' + value.toLocaleString('en-IN');
                        }
                    }
                }
            },
            plugins: {
                legend: {
                    display: true,
                    position: 'top',
                    labels: {
                        color: '#B8B8B8',
                        padding: 20,
                        usePointStyle: true,
                        font: {
                            family: "'Inter', sans-serif",
                            size: 12
                        }
                    }
                },
                tooltip: {
                    backgroundColor: 'rgba(31, 31, 31, 0.95)',
                    titleColor: '#fff',
                    bodyColor: '#fff',
                    borderColor: 'rgba(58, 134, 255, 0.5)',
                    borderWidth: 1,
                    padding: 12,
                    cornerRadius: 8,
                    callbacks: {
                        label: function (context) {
                            return `Potential: ₹${context.parsed.y.toLocaleString('en-IN')}`;
                        }
                    }
                }
            }
        }
    });
}

// Generate chart legend
function generateChartLegend(labels, colors) {
    const legendContainer = document.querySelector('.chart-legend');
    if (!legendContainer) return;

    legendContainer.innerHTML = labels.map((label, index) => `
    <div class="legend-item">
      <span class="legend-color" style="background-color: ${colors[index]}"></span>
      <span>${label}</span>
    </div>
  `).join('');
}

// Refresh recommendations
async function refreshRecommendations() {
    const refreshBtn = document.querySelector('.refresh-btn');
    const originalHtml = refreshBtn.innerHTML;

    refreshBtn.innerHTML = '<span class="btn-icon">⟳</span> Refreshing...';
    refreshBtn.disabled = true;

    try {
        const response = await fetch('/recommendations/refresh', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCSRFToken()
            }
        });

        const result = await response.json();

        if (result.success) {
            // Reload page to show new recommendations
            window.location.reload();
        } else {
            alert(result.message || 'Failed to refresh recommendations');
        }
    } catch (error) {
        console.error('Error refreshing:', error);
        alert('An error occurred while refreshing');
    } finally {
        refreshBtn.innerHTML = originalHtml;
        refreshBtn.disabled = false;
    }
}

// Get CSRF token
function getCSRFToken() {
    const meta = document.querySelector('meta[name="csrf-token"]');
    return meta ? meta.getAttribute('content') : '';
}

// Table row hover effect enhancement
document.querySelectorAll('.table-row').forEach(row => {
    row.addEventListener('mouseenter', function () {
        this.style.transform = 'translateX(4px)';
    });
    row.addEventListener('mouseleave', function () {
        this.style.transform = '';
    });
});
