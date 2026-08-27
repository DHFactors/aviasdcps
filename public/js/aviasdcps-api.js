/*
================================================================================
FILE: public/js/aviasdcps-api.js
VERSION: 0.3.0
PURPOSE: Tenant-aware REST API client for AVIA SDCPS — with full mock data
AUTHOR: AVIA Safety Systems Team
LAST UPDATED: 2026-08-27
================================================================================
*/

class AviaSDCPSAPI {
    constructor(baseURL = '') {
        this.baseURL = baseURL || window.location.origin;
        this.tenantId = localStorage.getItem('tenantId') || 'tenant-001';
        this.apiKey = localStorage.getItem('apiKey') || 'demo-key-001';
        this.useMock = true; // Enable mock data for demo
        console.log('✅ API Client initialized with tenant:', this.tenantId);
        console.log('📊 Using mock data for demo');
    }

    // ==================== MOCK DATA ====================
    getMockHazards() {
        return [
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
            },
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
                id: "haz-006",
                title: "Crew fatigue incident",
                description: "Flight crew reported fatigue after long-haul flight. Investigation into scheduling procedures initiated.",
                category: "Human Factors",
                severity: "High",
                probability: "Possible",
                risk_level: "High",
                status: "Open",
                owner: "Emily Davis",
                location: "Crew Briefing Room, Dubai Airport",
                created_at: new Date(Date.now() - 4 * 24 * 60 * 60 * 1000).toISOString(),
                updated_at: new Date(Date.now() - 3 * 24 * 60 * 60 * 1000).toISOString()
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
                location: "Maintenance Hangar, Singapore Airport",
                created_at: new Date(Date.now() - 15 * 24 * 60 * 60 * 1000).toISOString(),
                updated_at: new Date(Date.now() - 12 * 24 * 60 * 60 * 1000).toISOString()
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
            }
        ];
    }

    getMockMetrics() {
        return {
            tenant_id: "tenant-001",
            spi_values: {
                HRC: {
                    current: 1.2,
                    target: 1.5,
                    trend: "stable",
                    history: [1.1, 1.3, 1.2, 1.4, 1.2, 1.5]
                },
                SPT: {
                    current: 85.5,
                    target: 85,
                    trend: "up",
                    history: [78, 80, 82, 84, 85, 86]
                },
                ALoSP: {
                    current: 0.95,
                    target: 1.0,
                    trend: "stable",
                    history: [1.1, 1.0, 0.9, 0.95, 1.0, 0.98]
                }
            },
            last_updated: new Date().toISOString()
        };
    }

    getMockSPISPT() {
        return {
            dates: ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
            hrc: [1.2, 1.4, 1.3, 1.5, 1.6, 1.4],
            spt: [78, 80, 82, 85, 84, 86],
            alosp: [1.1, 1.0, 0.9, 0.95, 1.0, 0.98]
        };
    }

    getMockALoSP() {
        return {
            categories: ["Operational", "Technical", "Human Factors", "Environmental", "Organizational"],
            values: [1.2, 0.8, 1.1, 0.9, 1.0],
            target: 1.0
        };
    }

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
        console.log(`📡 ${options.method || 'GET'} request to:`, endpoint);

        // For demo, return mock data
        if (this.useMock) {
            await new Promise(resolve => setTimeout(resolve, 500)); // Simulate network delay
            return this.getMockResponse(endpoint, options);
        }

        // Real API call (for when backend is deployed)
        try {
            const url = `${this.baseURL}/api/v1${endpoint}`;
            const headers = {
                'Content-Type': 'application/json',
                'X-Tenant-Id': this.tenantId,
                'X-API-Key': this.apiKey,
                ...options.headers
            };
            const response = await fetch(url, { ...options, headers });
            if (!response.ok) throw new Error(`HTTP ${response.status}`);
            return response.json();
        } catch (error) {
            console.warn('API call failed, falling back to mock data:', error);
            return this.getMockResponse(endpoint, options);
        }
    }

    getMockResponse(endpoint, options) {
        if (endpoint.includes('hazards')) {
            if (options.method === 'POST') {
                return { success: true, message: "Hazard created", hazard: JSON.parse(options.body) };
            }
            return this.getMockHazards();
        }
        if (endpoint.includes('metrics')) return this.getMockMetrics();
        if (endpoint.includes('spi-spt')) return this.getMockSPISPT();
        if (endpoint.includes('alosp')) return this.getMockALoSP();
        if (endpoint.includes('audit')) return this.getMockAuditTrail();
        if (endpoint.includes('demo/status')) return this.getMockDemoStatus();
        if (endpoint.includes('demo/reset')) return { success: true, message: "Demo data reset" };
        return { message: "Mock response" };
    }

    // ==================== PUBLIC API METHODS ====================
    async getHazards(filters = {}) {
        return this.request('/hazards');
    }

    async createHazard(data) {
        return this.request('/hazards', { method: 'POST', body: JSON.stringify(data) });
    }

    async deleteHazard(id) {
        return this.request(`/hazards/${id}`, { method: 'DELETE' });
    }

    async getMetrics() {
        return this.request('/state-risk/metrics');
    }

    async getSPISPT(period = 'monthly') {
        return this.request(`/state-risk/spi-spt?period=${period}`);
    }

    async getALoSP() {
        return this.request('/state-risk/alosp');
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
}

const api = new AviaSDCPSAPI();
console.log('✅ AVIA SDCPS API Client loaded');
console.log('📋 Tenant:', api.tenantId);
console.log('📊 Mode:', api.useMock ? 'MOCK DATA' : 'REAL API');
