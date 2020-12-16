<template id="page-alunos">
	<div>
		[[message]]
		<hr>
		<div v-for="nacao,index in nacionalidades" key="nacao.sigla" style="margin-bottom:15px">
			<div>[[nacao.id]] - [[nacao.nome]]</div>
			<div>[[nacao.pais]] - [[nacao.sigla]]</div>
		</div>
	</div>
</template>

<script type="text/javascript">
	
	Vue.component('my-page-alunos',{
		template: '#page-alunos',
		props: {
		},
		delimiters: ['[[',']]'],
		data(){
			return {
				message:'Página Alunos',
				nacionalidades: [],
			}
		},
		methods:{
			getNacionalidades(){
				console.log('Requisição de nacionalidades')
				this.$http.get('/nacionalidades/').then(response => {
					this.nacionalidades = response.body;
					console.log('nacionalidades', this.nacionalidades)
				  }).catch( error => {
					this.nacionalidades = []
					console.log('Error', error)
				  });
			}
		},
		mounted(){
			this.getNacionalidades()
		},
		created(){
		},
		computed:{
			
		},
		watch:{
		}
	});
</script>