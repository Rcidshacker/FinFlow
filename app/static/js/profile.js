/**
 * Profile Page JavaScript
 * Edit modal and section editing functionality
 */

document.addEventListener('DOMContentLoaded', function () {
    // Edit section buttons
    const editButtons = document.querySelectorAll('.edit-section');
    const modal = document.getElementById('editModal');
    const modalTitle = document.querySelector('.modal-title');
    const modalBody = document.querySelector('.modal-body');
    const closeBtn = document.querySelector('.modal-close');
    const cancelBtn = document.querySelector('.cancel-edit');
    const saveBtn = document.querySelector('.save-edit');

    let currentSection = null;

    // Open edit modal
    editButtons.forEach(btn => {
        btn.addEventListener('click', function () {
            currentSection = this.dataset.section;
            openEditModal(currentSection);
        });
    });

    // Close modal handlers
    if (closeBtn) {
        closeBtn.addEventListener('click', closeModal);
    }
    if (cancelBtn) {
        cancelBtn.addEventListener('click', closeModal);
    }

    // Close on backdrop click
    if (modal) {
        modal.addEventListener('click', function (e) {
            if (e.target === this) {
                closeModal();
            }
        });
    }

    // Close on Escape key
    document.addEventListener('keydown', function (e) {
        if (e.key === 'Escape' && modal?.classList.contains('active')) {
            closeModal();
        }
    });

    // Save changes
    if (saveBtn) {
        saveBtn.addEventListener('click', saveChanges);
    }
});

// Open edit modal with appropriate form
function openEditModal(section) {
    const modal = document.getElementById('editModal');
    const modalTitle = document.querySelector('.modal-title');
    const modalBody = document.querySelector('.modal-body');

    if (!modal || !modalBody) return;

    // Set title based on section
    const titles = {
        personal: 'Edit Personal Information',
        financial: 'Edit Financial Overview',
        preferences: 'Edit Investment Preferences'
    };

    if (modalTitle) {
        modalTitle.textContent = titles[section] || 'Edit Profile';
    }

    // Generate form based on section
    modalBody.innerHTML = generateEditForm(section);

    // Show modal
    modal.classList.add('active');
    document.body.style.overflow = 'hidden';

    // Focus first input
    const firstInput = modalBody.querySelector('input, select');
    if (firstInput) {
        setTimeout(() => firstInput.focus(), 100);
    }
}

// Close modal
function closeModal() {
    const modal = document.getElementById('editModal');
    if (modal) {
        modal.classList.remove('active');
        document.body.style.overflow = '';
    }
}

// Generate edit form HTML based on section
function generateEditForm(section) {
    // Get current values from the page
    const forms = {
        personal: `
      <form id="editForm" data-section="${section}">
        <div class="form-group">
          <label for="edit-name">Full Name</label>
          <input type="text" id="edit-name" name="name" class="form-input" 
                 value="${getInfoValue('Name') || ''}" required>
        </div>
        <div class="form-row">
          <div class="form-group">
            <label for="edit-age">Age</label>
            <input type="number" id="edit-age" name="age" class="form-input" 
                   min="18" max="100" value="${getInfoValue('Age', true) || ''}" required>
          </div>
          <div class="form-group">
            <label for="edit-dependents">Dependents</label>
            <input type="number" id="edit-dependents" name="dependents" class="form-input" 
                   min="0" max="20" value="${getInfoValue('Dependents', true) || '0'}">
          </div>
        </div>
      </form>
    `,
        financial: `
      <form id="editForm" data-section="${section}">
        <div class="form-group">
          <label for="edit-investment">Investment Amount (₹)</label>
          <input type="number" id="edit-investment" name="investment_amount" class="form-input" 
                 min="1000" step="1000" value="${getInfoValue('Investment Amount', true) || ''}" required>
        </div>
        <div class="form-group">
          <label for="edit-income">Annual Income</label>
          <select id="edit-income" name="annual_income" class="form-select" required>
            <option value="">Select Range</option>
            <option value="0-5L" ${getInfoValue('Annual Income') === '0-5L' ? 'selected' : ''}>₹0 - ₹5 Lakhs</option>
            <option value="5-10L" ${getInfoValue('Annual Income') === '5-10L' ? 'selected' : ''}>₹5L - ₹10L</option>
            <option value="10-25L" ${getInfoValue('Annual Income') === '10-25L' ? 'selected' : ''}>₹10L - ₹25L</option>
            <option value="25-50L" ${getInfoValue('Annual Income') === '25-50L' ? 'selected' : ''}>₹25L - ₹50L</option>
            <option value="50L-1Cr" ${getInfoValue('Annual Income') === '50L-1Cr' ? 'selected' : ''}>₹50L - ₹1 Crore</option>
            <option value="1Cr+" ${getInfoValue('Annual Income') === '1Cr+' ? 'selected' : ''}>₹1 Crore+</option>
          </select>
        </div>
        <div class="form-row">
          <div class="form-group">
            <label for="edit-return">Expected Return (%)</label>
            <input type="number" id="edit-return" name="expected_return" class="form-input" 
                   min="0" max="100" step="0.5" value="${getInfoValue('Expected Return', true) || ''}" required>
          </div>
          <div class="form-group">
            <label for="edit-debt">Total Debt (₹)</label>
            <input type="number" id="edit-debt" name="total_debt" class="form-input" 
                   min="0" step="1000" value="${getInfoValue('Total Debt', true) || '0'}">
          </div>
        </div>
      </form>
    `,
        preferences: `
      <form id="editForm" data-section="${section}">
        <div class="form-group">
          <label>Risk Preference</label>
          <div class="radio-card-group">
            <label class="radio-card">
              <input type="radio" name="risk_preference" value="high" ${getCurrentRiskPreference() === 'high' ? 'checked' : ''}>
              <div class="radio-card-content">
                <span class="radio-icon">🔥</span>
                <span class="radio-label">High Risk</span>
              </div>
            </label>
            <label class="radio-card">
              <input type="radio" name="risk_preference" value="moderate" ${getCurrentRiskPreference() === 'moderate' ? 'checked' : ''}>
              <div class="radio-card-content">
                <span class="radio-icon">⚖️</span>
                <span class="radio-label">Moderate</span>
              </div>
            </label>
            <label class="radio-card">
              <input type="radio" name="risk_preference" value="low" ${getCurrentRiskPreference() === 'low' ? 'checked' : ''}>
              <div class="radio-card-content">
                <span class="radio-icon">🛡️</span>
                <span class="radio-label">Low Risk</span>
              </div>
            </label>
          </div>
        </div>
        <div class="form-group">
          <label>Investment Goals</label>
          <div class="radio-card-group horizontal">
            <label class="radio-card">
              <input type="radio" name="investment_goals" value="long_term" ${getCurrentGoals() === 'long_term' ? 'checked' : ''}>
              <div class="radio-card-content">
                <span class="radio-icon">📈</span>
                <span class="radio-label">Long-term</span>
              </div>
            </label>
            <label class="radio-card">
              <input type="radio" name="investment_goals" value="short_term" ${getCurrentGoals() === 'short_term' ? 'checked' : ''}>
              <div class="radio-card-content">
                <span class="radio-icon">⚡</span>
                <span class="radio-label">Short-term</span>
              </div>
            </label>
          </div>
        </div>
      </form>
    `
    };

    return forms[section] || '<p>Unable to load form</p>';
}

// Get info value from the page
function getInfoValue(label, isNumeric = false) {
    const items = document.querySelectorAll('.info-item');
    for (const item of items) {
        const labelEl = item.querySelector('.info-label');
        if (labelEl && labelEl.textContent.trim() === label) {
            const valueEl = item.querySelector('.info-value');
            if (valueEl) {
                let value = valueEl.textContent.trim();
                if (isNumeric) {
                    // Remove currency symbols and formatting
                    value = value.replace(/[₹,%\s]/g, '').replace(/,/g, '');
                    // Remove units like "years"
                    value = value.replace(/years?/i, '').trim();
                    return parseFloat(value) || 0;
                }
                return value;
            }
        }
    }
    return '';
}

// Get current risk preference
function getCurrentRiskPreference() {
    const badge = document.querySelector('.info-value .risk-badge');
    if (badge) {
        const text = badge.textContent.toLowerCase();
        if (text.includes('high')) return 'high';
        if (text.includes('moderate')) return 'moderate';
        if (text.includes('low')) return 'low';
    }
    return '';
}

// Get current investment goals
function getCurrentGoals() {
    const items = document.querySelectorAll('.info-item');
    for (const item of items) {
        const label = item.querySelector('.info-label');
        if (label && label.textContent.includes('Investment Goals')) {
            const value = item.querySelector('.info-value');
            if (value) {
                const text = value.textContent.toLowerCase();
                if (text.includes('long')) return 'long_term';
                if (text.includes('short')) return 'short_term';
            }
        }
    }
    return '';
}

// Save changes via AJAX
async function saveChanges() {
    const form = document.getElementById('editForm');
    if (!form) return;

    const section = form.dataset.section;
    const formData = new FormData(form);
    const updates = {};

    formData.forEach((value, key) => {
        updates[key] = value;
    });

    const saveBtn = document.querySelector('.save-edit');
    const originalText = saveBtn.textContent;
    saveBtn.textContent = 'Saving...';
    saveBtn.disabled = true;

    try {
        const response = await fetch('/profile/edit', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCSRFToken()
            },
            body: JSON.stringify({ section, updates })
        });

        const result = await response.json();

        if (result.success) {
            // Reload page to show updated data
            window.location.reload();
        } else {
            alert(result.message || 'Failed to save changes');
        }
    } catch (error) {
        console.error('Error saving profile:', error);
        alert('An error occurred while saving');
    } finally {
        saveBtn.textContent = originalText;
        saveBtn.disabled = false;
    }
}

// Get CSRF token from meta tag
function getCSRFToken() {
    const meta = document.querySelector('meta[name="csrf-token"]');
    return meta ? meta.getAttribute('content') : '';
}
