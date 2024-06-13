document.addEventListener('DOMContentLoaded', function() {
    
    // Adicione um listener de evento para o clique no ícone de exclusão
    document.querySelectorAll('.delete-icon').forEach(function(icon) {
        icon.addEventListener('click', function(e) {
            e.preventDefault();
            
            // Obtenha o ID do usuário a ser excluído do atributo data-id
            var usuarioId = this.getAttribute('data-id');
            console.log('Clicou no ícone de exclusão para o usuário com ID:', usuarioId); // Adicionando o log
           
            // Envie uma solicitação DELETE para a rota de exclusão
            fetch('/excluir/' + usuarioId, { method: 'DELETE' })
                .then(function(response) {

                    // Verifique se a exclusão foi bem-sucedida
                    if (response.ok) {
                        
                        // Redirecione o usuário para a página de conteúdo após a exclusão bem-sucedida
                        window.location.reload();
                        }
                    })
            .catch(function(error) {
                console.error('Erro ao excluir usuário:', error);
            });
        });
    });
});
