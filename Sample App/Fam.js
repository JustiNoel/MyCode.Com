function createMemberElement(member) {
    const memberDiv = document.createElement('div');
    memberDiv.classList.add('member');
    memberDiv.innerHTML = `<strong>${member.name}</strong><br>Age: ${member.age}`;
    return memberDiv;
}

function renderFamilyTree(family) {
    const familyTreeDiv = document.getElementById('family-tree');
    
    family.members.forEach(member => {
        const memberElement = createMemberElement(member);
        familyTreeDiv.appendChild(memberElement);
    });
}

renderFamilyTree(family);