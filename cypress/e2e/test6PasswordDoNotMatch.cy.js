describe('User Registration', () => {
  beforeEach(() => {
    cy.visit('https://test-qa.inlaze.com/auth/sign-up');
  });

  it('should show error message when passwords do not match ', () => {
    
    cy.get('#full-name').type('Daniel Fernando Romero Ochoa');
    cy.get('#email').type('danielrmo95@gmail.com');

    cy.get('#password').type('Bogotac1.');
    cy.get('#confirm-password').type('Bogotac1');
    cy.get('span.label-text-alt.text-error').should('contain.text', 'Passwords do not match');
 
  });
});




