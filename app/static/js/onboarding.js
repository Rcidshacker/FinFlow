/**
 * Onboarding Form Logic
 * Multi-step form handling with validation
 */

document.addEventListener('DOMContentLoaded', function () {
    // Range slider sync with input
    const rangeSliders = document.querySelectorAll('.range-slider input[type="range"]');
    rangeSliders.forEach(slider => {
        const input = slider.closest('.form-group').querySelector('.form-input');
        if (input) {
            // Sync slider to input
            slider.addEventListener('input', function () {
                input.value = this.value;
            });

            // Sync input to slider
            input.addEventListener('input', function () {
                slider.value = this.value;
            });
        }
    });

    // Form validation
    const forms = document.querySelectorAll('.onboarding-form');
    forms.forEach(form => {
        form.addEventListener('submit', function (e) {
            if (!validateForm(this)) {
                e.preventDefault();
            }
        });
    });

    // Real-time validation on blur
    const inputs = document.querySelectorAll('.form-input, .form-select');
    inputs.forEach(input => {
        input.addEventListener('blur', function () {
            validateField(this);
        });
    });

    // Radio card selection visual feedback
    const radioCards = document.querySelectorAll('.radio-card input');
    radioCards.forEach(radio => {
        radio.addEventListener('change', function () {
            // Remove selected state from siblings
            const group = this.closest('.radio-card-group, .answer-options');
            if (group) {
                group.querySelectorAll('.radio-card-content, .option-content').forEach(content => {
                    content.classList.remove('selected');
                });

                // Add selected state to current
                const content = this.nextElementSibling;
                if (content) {
                    content.classList.add('selected');
                }
            }
        });
    });

    // Answer option selection (questionnaire)
    const answerOptions = document.querySelectorAll('.answer-option input');
    answerOptions.forEach(option => {
        option.addEventListener('change', function () {
            const block = this.closest('.question-block');
            if (block) {
                block.querySelectorAll('.option-content').forEach(content => {
                    content.classList.remove('selected');
                });
                this.nextElementSibling.classList.add('selected');
            }
        });
    });

    // Multi-select enhancement
    const multiSelects = document.querySelectorAll('.form-select-multi');
    multiSelects.forEach(select => {
        // Show selected count
        select.addEventListener('change', function () {
            const count = this.selectedOptions.length;
            const hint = this.closest('.form-group').querySelector('.multi-select-hint');
            if (hint) {
                hint.textContent = `${count} selected (hold Ctrl/Cmd to select multiple)`;
            }
        });
    });
});

// Validate single field
function validateField(field) {
    const value = field.value.trim();
    const isRequired = field.hasAttribute('required');

    // Clear previous errors
    clearFieldError(field);

    // Required check
    if (isRequired && !value) {
        showFieldError(field, 'This field is required');
        return false;
    }

    // Email validation
    if (field.type === 'email' && value) {
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailRegex.test(value)) {
            showFieldError(field, 'Please enter a valid email address');
            return false;
        }
    }

    // Number validation
    if (field.type === 'number' && value) {
        const num = parseFloat(value);
        const min = parseFloat(field.getAttribute('min'));
        const max = parseFloat(field.getAttribute('max'));

        if (!isNaN(min) && num < min) {
            showFieldError(field, `Value must be at least ${min}`);
            return false;
        }
        if (!isNaN(max) && num > max) {
            showFieldError(field, `Value must be at most ${max}`);
            return false;
        }
    }

    // Mark as valid
    field.classList.add('valid');
    return true;
}

// Validate entire form
function validateForm(form) {
    let isValid = true;
    const fields = form.querySelectorAll('.form-input[required], .form-select[required]');

    fields.forEach(field => {
        if (!validateField(field)) {
            isValid = false;
        }
    });

    // Check radio buttons
    const radioGroups = form.querySelectorAll('.radio-card-group, .answer-options');
    radioGroups.forEach(group => {
        const radios = group.querySelectorAll('input[type="radio"]');
        const isRequired = radios[0]?.hasAttribute('required');

        if (isRequired) {
            const isChecked = Array.from(radios).some(r => r.checked);
            if (!isChecked) {
                isValid = false;
                // Show error on group
                group.classList.add('error');
            } else {
                group.classList.remove('error');
            }
        }
    });

    return isValid;
}

// Show field error
function showFieldError(field, message) {
    field.classList.add('invalid');
    field.classList.remove('valid');

    // Remove existing error
    const existingError = field.parentNode.querySelector('.field-error');
    if (existingError) {
        existingError.remove();
    }

    // Add error message
    const errorEl = document.createElement('span');
    errorEl.className = 'field-error';
    errorEl.textContent = message;
    field.parentNode.appendChild(errorEl);
}

// Clear field error
function clearFieldError(field) {
    field.classList.remove('invalid');
    const error = field.parentNode.querySelector('.field-error');
    if (error) {
        error.remove();
    }
}

// Format currency input
function formatCurrency(input) {
    let value = input.value.replace(/[^\d]/g, '');
    if (value) {
        value = parseInt(value).toLocaleString('en-IN');
        input.value = value;
    }
}
