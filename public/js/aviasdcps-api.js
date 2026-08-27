/*
================================================================================
FILE: public/js/aviasdcps-api.js
VERSION: 0.2.0
PURPOSE: Tenant-aware REST API client for AVIA SDCPS
AUTHOR: AVIA Safety Systems Team
LAST UPDATED: 2026-08-27
================================================================================
*/

class AviaSDCPSAPI {
    constructor(baseURL = '') {
        this.baseURL = baseURL || window.location.origin;
        this.tenantId = localStorage.getItem('tenantId') || 'tenant-001';
        this.apiKey = localStorage.getItem('apiKey') || 'demo-key-001';
    }
    
    async request(endpoint, options = {}) {
        const url = `${this.baseURL}/api/v1${endpoint}`;
        const headers = {
            'Content-Type': 'application/json',
            'X-Tenant-Id': this.tenantId,
            'X-API-Key': this.apiKey,
            ...options.headers
        };
        
        try {
            const response = await fetch(url, {
                ...options,
                headers
            });
            
            if (!response.ok) {
                const error = await response.json().catch(() => ({}));
                throw new Error(error.detail || `HTTP ${response.status}`);
            }
            
            return response.json();
        } catch (error) {
            console.error(`API Error [${endpoint}]:`, error);
            throw error;
        }
    }
    
    // ==================== HAZARDS ====================
    async getHazards(filters = {}) {
        const params = new URLSearchParams(filters);
        return this.request(`/hazards?${params.toString()}`);
    }
    
    async createHazard(data) {
        return this.request('/hazards', {
            method: 'POST',
            body: JSON.stringify(data)
        });
    }
    
    // ==================== State Oversight ====================
    async getMetrics() {
        return this.request('/state-risk/metrics');
    }
    
    async getSPISPT(period = 'monthly') {
        return this.request(`/state-risk/spi-spt?period=${period}`);
    }
    
    async getALoSP() {
        return this.request('/state-risk/alosp');
    }
    
    // ==================== DEMO ====================
    async getDemoStatus() {
        return this.request('/demo/status');
    }
    
    async resetDemoData() {
        return this.request('/demo/reset-data', {
            method: 'POST'
        });
    }
}

// Create global instance
const api = new AviaSDCPSAPI();

console.log('✅ AVIA SDCPS API Client loaded');
console.log(`📋 Tenant: ${api.tenantId}`);
console.log(`🔑 API Key: ${api.apiKey}`);