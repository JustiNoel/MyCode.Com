const family = {
    name: "Smith",
    members: [
        {
            id: 1,
            name: "John Smith",
            age: 50,
            relationships: {
                spouse: 2,
                children: [3, 4]
            }
        },
        {
            id: 2,
            name: "Jane Smith",
            age: 48,
            relationships: {
                spouse: 1,
                children: [3, 4]
            }
        },
        {
            id: 3,
            name: "Emily Smith",
            age: 20,
            relationships: {
                parents: [1, 2]
            }
        },
        {
            id: 4,
            name: "Michael Smith",
            age: 18,
            relationships: {
                parents: [1, 2]
            }
        }
    ]
};