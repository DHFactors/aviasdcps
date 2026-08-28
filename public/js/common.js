// ==================== SIDEBAR ====================
function loadSidebar() {
    fetch('/views/sidebar.html')
        .then(response => response.text())
        .then(html => {
            document.getElementById('sidebar-container').innerHTML = html;
            highlightActiveNav();
            updateSidebarUser();
            updateSidebarView();
        });
}

function highlightActiveNav() {
    const currentPage = window.location.pathname.split('/').pop();
    document.querySelectorAll('.sidebar-nav .nav-item').forEach(item => {
        item.classList.remove('active');
        if (item.getAttribute('href') === '/' + currentPage || item.getAttribute('href') === currentPage) {
            item.classList.add('active');
        }
    });
}

function switchTenant(tenantId) {
    localStorage.setItem('tenantId', tenantId);
    updateSidebarUser(tenantId);
    window.location.reload();
}

// ==================== USER ====================
function updateSidebarUser(tenantId) {
    const tid = tenantId || localStorage.getItem('tenantId') || 'tenant-001';
    const tenantNames = {
        'tenant-001': 'Pacific Air Services',
        'tenant-002': 'Nordic Aviation Group',
        'tenant-003': 'Southern Hemisphere Airlines'
    };
    const name = tenantNames[tid] || tid;
    const el = document.getElementById('sidebarUserTenant');
    if (el) el.textContent = name;
    const sel = document.getElementById('tenantSelector');
    if (sel) sel.value = tid;
}

function updateSidebarView(page) {
    const viewDetail = document.getElementById('sidebarViewDetail');
    if (!viewDetail) return;
    const p = page || window.location.pathname.split('/').pop().replace('.html','');
    if (p === 'state-oversight' || p === 'state') {
        viewDetail.textContent = 'State Oversight (All Tenants)';
    } else if (p === 'dashboard') {
        viewDetail.textContent = 'Dashboard · Tenant view';
    } else {
        viewDetail.textContent = 'Tenant view';
    }
}

// ==================== SIDEBAR TOGGLE ====================
function toggleSidebar() {
    const sidebar = document.querySelector('.sidebar');
    const overlay = document.querySelector('.sidebar-overlay');
    if (sidebar) sidebar.classList.toggle('open');
    if (overlay) overlay.classList.toggle('active');
}
function closeSidebar() {
    const sidebar = document.querySelector('.sidebar');
    const overlay = document.querySelector('.sidebar-overlay');
    if (sidebar) sidebar.classList.remove('open');
    if (overlay) overlay.classList.remove('active');
}

// ==================== LOGOUT ====================
function logoutUser() {
    localStorage.removeItem('isLoggedIn');
    localStorage.removeItem('tenantId');
    window.location.href = '/login.html';
}

// ==================== TENANT ====================
function getCurrentTenant() {
    return localStorage.getItem('tenantId') || 'tenant-001';
}

function getTenantName(tenantId) {
    const names = {
        'tenant-001': 'Pacific Air Services',
        'tenant-002': 'Nordic Aviation Group',
        'tenant-003': 'Southern Hemisphere Airlines'
    };
    return names[tenantId] || tenantId;
}
