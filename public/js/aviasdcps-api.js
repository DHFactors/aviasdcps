/*
================================================================================
FILE: public/js/aviasdcps-api.js
VERSION: 0.4.0
PURPOSE: Tenant-aware REST API client — multi-tenant mock data
AUTHOR: AVIA Safety Systems Team
LAST UPDATED: 2026-08-27
================================================================================
*/

class AviaSDCPSAPI {
    constructor(baseURL = '') {
        this.baseURL = baseURL || window.location.origin;
        this.tenantId = localStorage.getItem('tenantId') || 'tenant-001';
        this.apiKey = localStorage.getItem('apiKey') || 'demo-key-001';
        this.useMock = true;
        console.log('✅ API Client initialized with tenant:', this.tenantId);
        console.log('📊 Mode: MOCK DATA (multi-tenant)');
        this.tenantNames = {
            'tenant-001': 'Pacific Air Services',
            'tenant-002': 'Nordic Aviation Group',
            'tenant-003': 'Southern Hemisphere Airlines'
        };
    }

    // ==================== MOCK DATA - TENANT ISOLATED ====================
    getTenantHazards(tenantId) {
        const id = tenantId || this.tenantId;
        const map = {
            'tenant-001': [
            {
                id: "haz-001",
                title: "Bird strike risk on runway 27L",
                description: "Multiple bird sightings during morning hours near runway 27L. Potential risk to departing aircraft.",
                category: "Operational",
                severity: "High",
                probability: "Likely",
                risk_level: "High",
                status: "Open",
                owner: "John Smith",
                location: "Runway 27L, Sydney Airport",
                created_at: new Date(Date.now() - 2 * 24 * 60 * 60 * 1000).toISOString(),
                updated_at: new Date(Date.now() - 1 * 24 * 60 * 60 * 1000).toISOString()
            },
            {
                id: "haz-002",
                title: "Runway debris incident",
                description: "Foreign object debris (FOD) found on runway after landing. Debris identified as metal fragments.",
                category: "Operational",
                severity: "Medium",
                probability: "Possible",
                risk_level: "Medium",
                status: "Under Review",
                owner: "Jane Doe",
                location: "Runway 27L, Sydney Airport",
                created_at: new Date(Date.now() - 5 * 24 * 60 * 60 * 1000).toISOString(),
                updated_at: new Date(Date.now() - 3 * 24 * 60 * 60 * 1000).toISOString()
            },
            {
                id: "haz-003",
                title: "Fuel contamination discovered",
                description: "Water and sediment found in fuel sample during pre-flight inspection. Affected batch quarantined.",
                category: "Technical",
                severity: "Critical",
                probability: "Rare",
                risk_level: "High",
                status: "Open",
                owner: "Mike Johnson",
                location: "Fuel Farm, Sydney Airport",
                created_at: new Date(Date.now() - 1 * 24 * 60 * 60 * 1000).toISOString(),
                updated_at: new Date(Date.now() - 1 * 24 * 60 * 60 * 1000).toISOString()
            },
            {
                id: "haz-004",
                title: "ATC communication breakdown",
                description: "Temporary loss of communication between tower and arriving aircraft during busy period.",
                category: "Human Factors",
                severity: "High",
                probability: "Unlikely",
                risk_level: "Medium",
                status: "Closed",
                owner: "Sarah Williams",
                location: "Control Tower, Sydney Airport",
                created_at: new Date(Date.now() - 10 * 24 * 60 * 60 * 1000).toISOString(),
                updated_at: new Date(Date.now() - 8 * 24 * 60 * 60 * 1000).toISOString()
            }
            ],
            'tenant-002': [
            {
                id: "haz-005",
                title: "De-icing fluid shortage",
                description: "Supply chain disruption causing shortage of de-icing fluid during peak winter operations.",
                category: "Organizational",
                severity: "Medium",
                probability: "Possible",
                risk_level: "Medium",
                status: "Under Review",
                owner: "Robert Chen",
                location: "Maintenance Hangar, Oslo Airport",
                created_at: new Date(Date.now() - 3 * 24 * 60 * 60 * 1000).toISOString(),
                updated_at: new Date(Date.now() - 2 * 24 * 60 * 60 * 1000).toISOString()
            },
            {
                id: "haz-007",
                title: "Hydraulic system leak",
                description: "Minor hydraulic fluid leak detected during routine maintenance. Component scheduled for replacement.",
                category: "Technical",
                severity: "Medium",
                probability: "Unlikely",
                risk_level: "Low",
                status: "Closed",
                owner: "David Park",
                location: "Maintenance Hangar, Oslo Airport",
                created_at: new Date(Date.now() - 15 * 24 * 60 * 60 * 1000).toISOString(),
                updated_at: new Date(Date.now() - 12 * 24 * 60 * 60 * 1000).toISOString()
            },
            {
                id: "haz-009",
                title: "Emergency evacuation drill incomplete",
                description: "Monthly emergency evacuation drill identified gaps in response time and communication protocols.",
                category: "Organizational",
                severity: "High",
                probability: "Possible",
                risk_level: "High",
                status: "Open",
                owner: "Mark Wilson",
                location: "Terminal 3, Oslo Airport",
                created_at: new Date(Date.now() - 6 * 24 * 60 * 60 * 1000).toISOString(),
                updated_at: new Date(Date.now() - 4 * 24 * 60 * 60 * 1000).toISOString()
            }
            ],
            'tenant-003': [
            {
                id: "haz-006",
                title: "Crew fatigue incident",
                description: "Flight crew reported fatigue after long-haul flight. Investigation into scheduling procedures initiated.",
                category: "Human Factors",
                severity: "High",
                probability: "Possible",
                risk_level: "High",
                status: "Open",
                owner: "Emily Davis",
                location: "Crew Briefing Room, Johannesburg Airport",
                created_at: new Date(Date.now() - 4 * 24 * 60 * 60 * 1000).toISOString(),
                updated_at: new Date(Date.now() - 3 * 24 * 60 * 60 * 1000).toISOString()
            },
            {
                id: "haz-008",
                title: "Weather diversion - severe thunderstorm",
                description: "Inbound flight diverted due to severe thunderstorm activity near airport. Holding procedures initiated.",
                category: "Environmental",
                severity: "Medium",
                probability: "Possible",
                risk_level: "Medium",
                status: "Closed",
                owner: "Lisa Thompson",
                location: "Approach Control, Johannesburg Airport",
                created_at: new Date(Date.now() - 7 * 24 * 60 * 60 * 1000).toISOString(),
                updated_at: new Date(Date.now() - 5 * 24 * 60 * 60 * 1000).toISOString()
            },
            {
                id: "haz-010",
                title: "Navigation system anomaly",
                description: "GPS navigation system reported intermittent signal loss during approach in specific weather conditions.",
                category: "Technical",
                severity: "Critical",
                probability: "Rare",
                risk_level: "High",
                status: "Under Review",
                owner: "Dr. Alan Chen",
                location: "Approach Corridor, Johannesburg Airport",
                created_at: new Date(Date.now() - 2 * 24 * 60 * 60 * 1000).toISOString(),
                updated_at: new Date(Date.now() - 1 * 24 * 60 * 60 * 1000).toISOString()
            }
            ]
        };
        return map[id] || map['tenant-001'];
    }

    getAllHazards() {
        return [...this.getTenantHazards('tenant-001'), ...this.getTenantHazards('tenant-002'), ...this.getTenantHazards('tenant-003')];
    }

    getAggregatedHazards() {
        return this.getAllHazards();
    }

    getMockHazards(tenantId) {
        // Filtered by tenant — dashboard/hazards show only selected tenant
        if (tenantId === 'all' || tenantId === 'aggregated') return this.getAllHazards();
        return this.getTenantHazards(tenantId);
    }

    getMockMetrics(tenantId) {
        const id = tenantId || this.tenantId;
        const metricsMap = {
            'tenant-001': { current: { HRC: 1.2, SPT: 85.5, ALoSP: 0.95 }, trend: { HRC: 'stable', SPT: 'up', ALoSP: 'stable' }, baseline: { HRC: 1.8, SPT: 78, ALoSP: 1.2 }, unit: { HRC: 'Rate per 100,000 flights', SPT: 'Percentage', ALoSP: 'Rate per 100,000 flights' } },
            'tenant-002': { current: { HRC: 1.5, SPT: 82.0, ALoSP: 1.1 }, trend: { HRC: 'up', SPT: 'stable', ALoSP: 'up' }, baseline: { HRC: 1.9, SPT: 75, ALoSP: 1.3 }, unit: { HRC: 'Rate per 100,000 flights', SPT: 'Percentage', ALoSP: 'Rate per 100,000 flights' } },
            'tenant-003': { current: { HRC: 0.8, SPT: 78.0, ALoSP: 1.3 }, trend: { HRC: 'down', SPT: 'down', ALoSP: 'stable' }, baseline: { HRC: 1.4, SPT: 72, ALoSP: 1.5 }, unit: { HRC: 'Rate per 100,000 flights', SPT: 'Percentage', ALoSP: 'Rate per 100,000 flights' } }
        };
        const m = metricsMap[id] || metricsMap['tenant-001'];
        return {
            tenant_id: id,
            tenant_name: this.tenantNames[id],
            declared_spis: {
                HRC: { target: 1.5, current: m.current.HRC, unit: m.unit.HRC, baseline: m.baseline.HRC, declaration_date: '2026-01-01', review_date: '2026-12-31' },
                SPT: { target: 85, current: m.current.SPT, unit: m.unit.SPT, baseline: m.baseline.SPT, declaration_date: '2026-01-01', review_date: '2026-12-31' },
                ALoSP: { target: 1.0, current: m.current.ALoSP, unit: m.unit.ALoSP, baseline: m.baseline.ALoSP, declaration_date: '2026-01-01', review_date: '2026-12-31' }
            },
            spi_values: {
                HRC: { current: m.current.HRC, target: 1.5, trend: m.trend.HRC, history: [m.current.HRC-0.1, m.current.HRC+0.1, m.current.HRC, m.current.HRC+0.2, m.current.HRC, m.current.HRC+0.3], unit: m.unit.HRC, baseline: m.baseline.HRC, declaration_date: '2026-01-01', review_date: '2026-12-31' },
                SPT: { current: m.current.SPT, target: 85, trend: m.trend.SPT, history: [m.current.SPT-7, m.current.SPT-5, m.current.SPT-3, m.current.SPT-1, m.current.SPT, m.current.SPT+0.5], unit: m.unit.SPT, baseline: m.baseline.SPT, declaration_date: '2026-01-01', review_date: '2026-12-31' },
                ALoSP: { current: m.current.ALoSP, target: 1.0, trend: m.trend.ALoSP, history: [m.current.ALoSP+0.15, m.current.ALoSP+0.05, m.current.ALoSP-0.05, m.current.ALoSP, m.current.ALoSP+0.02, m.current.ALoSP], unit: m.unit.ALoSP, baseline: m.baseline.ALoSP, declaration_date: '2026-01-01', review_date: '2026-12-31' }
            },
            last_updated: new Date().toISOString()
        };
    }

    getAggregatedMetrics() {
        // State Oversight — aggregated across all tenants
        const avgHRC = (1.2 + 1.5 + 0.8) / 3;
        const avgSPT = (85.5 + 82.0 + 78.0) / 3;
        const avgALoSP = (0.95 + 1.1 + 1.3) / 3;
        return {
            tenant_id: 'all',
            tenant_name: 'All Tenants (State Oversight)',
            total_hazards: this.getAllHazards().length,
            breakdown: {
                'tenant-001': this.getTenantHazards('tenant-001').length,
                'tenant-002': this.getTenantHazards('tenant-002').length,
                'tenant-003': this.getTenantHazards('tenant-003').length
            },
            spi_values: {
                HRC: { current: parseFloat(avgHRC.toFixed(2)), target: 1.5, trend: 'stable', history: [1.1, 1.3, 1.2, 1.4, 1.17, 1.5] },
                SPT: { current: parseFloat(avgSPT.toFixed(1)), target: 85, trend: 'stable', history: [78, 80, 81, 82, 81.8, 83] },
                ALoSP: { current: parseFloat(avgALoSP.toFixed(2)), target: 1.0, trend: 'stable', history: [1.1, 1.05, 1.0, 1.12, 1.1, 1.12] }
            },
            last_updated: new Date().toISOString()
        };
    }

    getMockSPISPT(tenantId) {
        const map = {
            'tenant-001': { dates: ["Jan","Feb","Mar","Apr","May","Jun"], hrc: [1.1,1.3,1.2,1.4,1.2,1.5], spt: [80,82,83,84,85,85.5], alosp: [1.0,0.98,0.96,0.95,0.96,0.95] },
            'tenant-002': { dates: ["Jan","Feb","Mar","Apr","May","Jun"], hrc: [1.3,1.4,1.5,1.4,1.5,1.5], spt: [78,79,80,81,82,82], alosp: [1.0,1.05,1.08,1.1,1.09,1.1] },
            'tenant-003': { dates: ["Jan","Feb","Mar","Apr","May","Jun"], hrc: [0.9,0.8,0.85,0.8,0.78,0.8], spt: [75,76,77,78,77.5,78], alosp: [1.2,1.25,1.3,1.28,1.3,1.3] },
            'aggregated': { dates: ["Jan","Feb","Mar","Apr","May","Jun"], hrc: [1.2, 1.3, 1.4, 1.2, 1.3, 1.17], spt: [82.0, 80.5, 81.2, 82.5, 81.8, 81.8], alosp: [1.15, 1.12, 1.1, 1.08, 1.12, 1.12] }
        };
        if (tenantId === 'aggregated' || tenantId === 'all') return map['aggregated'];
        return map[tenantId || this.tenantId] || map['tenant-001'];
    }

    getAggregatedSPISPT() { return this.getMockSPISPT('aggregated'); }

    getMockALoSP(tenantId) {
        const map = {
            'tenant-001': { categories: ["Operational","Technical","Human Factors","Environmental","Organizational"], values: [1.1,0.9,1.0,0.8,0.95], target: 1.0 },
            'tenant-002': { categories: ["Operational","Technical","Human Factors","Environmental","Organizational"], values: [0.9,1.0,0.8,1.1,1.1], target: 1.0 },
            'tenant-003': { categories: ["Operational","Technical","Human Factors","Environmental","Organizational"], values: [1.0,1.3,1.2,0.9,1.1], target: 1.0 },
            'aggregated': { categories: ["Operational","Technical","Human Factors","Environmental","Organizational"], values: [1.0,1.07,1.0,0.93,1.05], target: 1.0 }
        };
        if (tenantId === 'aggregated' || tenantId === 'all') return map['aggregated'];
        return map[tenantId || this.tenantId] || map['tenant-001'];
    }

    getAggregatedALoSP() { return this.getMockALoSP('aggregated'); }

    getMockAuditTrail() {
        const actions = ['CREATE', 'UPDATE', 'VIEW', 'EXPORT', 'DELETE'];
        const entities = ['hazard', 'report', 'user', 'tenant'];
        const users = ['admin@aviasafe.com', 'analyst@aviasafe.com', 'viewer@aviasafe.com'];
        return Array.from({ length: 25 }, (_, i) => ({
            timestamp: new Date(Date.now() - i * 3600000 * Math.random() * 10).toISOString(),
            action: actions[Math.floor(Math.random() * actions.length)],
            entity_type: entities[Math.floor(Math.random() * entities.length)],
            user: users[Math.floor(Math.random() * users.length)],
            details: `ID: ${Math.random().toString(36).substring(7)}`
        }));
    }

    getMockDemoStatus() {
        return {
            demo_mode: true,
            refresh_interval: 300,
            reset_on_startup: true,
            active_sessions: 5,
            max_sessions: 50,
            timestamp: new Date().toISOString()
        };
    }

    // ==================== API METHODS ====================
    async request(endpoint, options = {}) {
        console.log(`📡 ${options.method || 'GET'} request to:`, endpoint, 'tenant:', this.tenantId);
        
        // ALWAYS use mock data - skip real API calls
        await new Promise(resolve => setTimeout(resolve, 300));
        
        console.log('🔍 Returning mock data for:', endpoint);
        return this.getMockResponse(endpoint, options);
    }

    getMockResponse(endpoint, options) {
        const tenant = this.tenantId;
        if (endpoint.includes('hazards')) {
            if (options.method === 'POST') {
                return { success: true, message: "Hazard created", hazard: JSON.parse(options.body) };
            }
            // Dashboard/Hazards filtered by tenant
            return this.getMockHazards(tenant);
        }
        if (endpoint.includes('metrics')) return this.getMockMetrics(tenant);
        if (endpoint.includes('spi-spt')) {
            if (endpoint.includes('aggregated')) return this.getAggregatedSPISPT();
            return this.getMockSPISPT(tenant);
        }
        if (endpoint.includes('alosp')) {
            if (endpoint.includes('aggregated')) return this.getAggregatedALoSP();
            return this.getMockALoSP(tenant);
        }
        if (endpoint.includes('audit')) return this.getMockAuditTrail();
        if (endpoint.includes('demo/status')) return this.getMockDemoStatus();
        if (endpoint.includes('demo/reset')) return { success: true, message: "Demo data reset" };
        if (endpoint.includes('state-risk/aggregated')) return this.getAggregatedMetrics();
        return { message: "Mock response" };
    }

    // ==================== PUBLIC API METHODS ====================
    async getHazards(filters = {}) {
        // respect tenant filter if provided
        const tenant = filters.tenant || this.tenantId;
        if (filters.aggregated) return this.getAllHazards();
        return this.getMockHazards(tenant);
    }

    async createHazard(data) {
        return this.request('/hazards', { method: 'POST', body: JSON.stringify(data) });
    }

    async deleteHazard(id) {
        return this.request(`/hazards/${id}`, { method: 'DELETE' });
    }

    async getMetrics(tenantId) {
        return this.getMockMetrics(tenantId || this.tenantId);
    }

    async getAggregatedMetrics() {
        // State Oversight aggregated
        return this.getAggregatedMetrics();
    }

    async getSPISPT(period = 'monthly', tenantId) {
        return this.getMockSPISPT(tenantId || this.tenantId);
    }

    async getAggregatedSPISPT() {
        return this.getMockSPISPT('aggregated');
    }

    async getALoSP(tenantId) {
        return this.getMockALoSP(tenantId || this.tenantId);
    }

    async getAggregatedALoSP() {
        return this.getMockALoSP('aggregated');
    }

    async getDemoStatus() {
        return this.request('/demo/status');
    }

    async resetDemoData() {
        return this.request('/demo/reset-data', { method: 'POST' });
    }

    async getRecentEmails() {
        return this.request('/email-preview/recent');
    }

    getTenantName(tenantId) {
        return this.tenantNames[tenantId || this.tenantId] || tenantId;
    }
}

const api = new AviaSDCPSAPI();
console.log('✅ AVIA SDCPS API Client loaded');
console.log('📋 Tenant:', api.tenantId, api.getTenantName());
console.log('📊 Mode:', api.useMock ? 'MOCK DATA (multi-tenant)' : 'REAL API');
