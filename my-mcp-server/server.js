const express = require('express');
const bodyParser = require('body-parser');

const app = express();
app.use(bodyParser.json());

// Enhanced mock data for SAP operations
const mockData = {
    products: [
        { id: "P001", name: "Product 1", price: 100, unit: "EA", plant: "1000" },
        { id: "P002", name: "Product 2", price: 200, unit: "EA", plant: "1000" }
    ],
    inventory: [
        { productId: "P001", plant: "1000", quantity: 50, unit: "EA" },
        { productId: "P002", plant: "1000", quantity: 30, unit: "EA" }
    ],
    salesOrders: [
        { 
            orderId: "SO001", 
            customerNumber: "CUST001",
            items: [{ productId: "P001", quantity: 10 }],
            status: "Open"
        }
    ],
    deliveries: []
};

// Enhanced MCP endpoints
app.post('/mcp/query', (req, res) => {
    const { operation, parameters } = req.body;
    console.log(`Received operation: ${operation}`, parameters);
    
    switch(operation) {
        case 'getProducts':
        case 'getAllProducts':
            return res.json({ success: true, data: mockData.products });

        case 'checkInventory':
            const { productId, plant } = parameters || {};
            const stock = mockData.inventory.find(
                item => item.productId === productId && item.plant === plant
            );
            return res.json({ success: true, data: stock });

        case 'createSalesOrder':
            const newOrder = {
                orderId: `SO${(mockData.salesOrders.length + 1).toString().padStart(3, '0')}`,
                ...parameters,
                status: "Open"
            };
            mockData.salesOrders.push(newOrder);
            return res.json({ success: true, data: newOrder });

        case 'getSalesOrders':
            return res.json({ success: true, data: mockData.salesOrders });

        default:
            return res.json({ 
                success: false, 
                error: `Operation "${operation}" not supported` 
            });
    }
});

// Health check endpoint
app.get('/health', (req, res) => {
    res.json({ status: 'healthy' });
});

const PORT = 3000;
app.listen(PORT, () => {
    console.log(`MCP Server running on http://localhost:${PORT}`);
});