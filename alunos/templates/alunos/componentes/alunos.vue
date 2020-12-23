<template id="page-alunos">
	<div>
		[[message]]
		<hr>
		<div v-for="nacao,index in nacionalidades" :key="nacao.sigla" style="margin-bottom:15px">
			<div>[[nacao.id]] - [[nacao.nome]]</div>
			<div>[[nacao.pais]] - [[nacao.sigla]]</div>
			<div><small>[[nacao.rud_url]]</small></div>
			<div style="margin-bottom: 5px">
				<button @click="deleteNacionalidade(nacao)">x</button>
			</div>
		</div>
		<form>
			Nacionalidade: [[ novaNacionalidade.nome ]] - [[ novaNacionalidade.pais ]] - [[ novaNacionalidade.sigla ]] 
			<div>
				<input type="text" placeholder="Nome: " v-model="novaNacionalidade.nome"/>
				<input type="text" placeholder="País: "  v-model="novaNacionalidade.pais" />
				<input type="text" placeholder="Sigla: " v-model="novaNacionalidade.sigla" />
				<button @click="postNacionalidade()">Adicionar</button>
			</div>
		</form>
		<hr>
		<div v-for="aluno,index in alunos" :key="aluno.matricula" style="margin-bottom:15px">
			<div> 
				[[aluno.matricula]]  - [[aluno.nome]] - [[aluno.get_nacionalidade]]
				<button @click="deleteAluno(aluno)">x</button>
				<hr>
			</div>

		</div>
		<hr>

		<div>
			<form>
				Alunos: [[novoAluno.matricula]] - [[novoAluno.nome]] - [[novoAluno.nacionalidade]]
				<div>
					<input type="text" placeholder="Matricula" v-model="novoAluno.matricula"/>
					<input type="text" placeholder="Nome" v-model="novoAluno.nome"/>
					<select v-model="novoAluno.nacionalidade">
						<option :key="nacao.id" v-for="nacao in nacionalidades" :value="nacao.id"> [[nacao.nome]] </option>
					</select>
					<button @click="postNovoAluno()">Adicionar</button>

				</div>
				

			</form>
		</div>

		<div v-for=" disc, index_disc in disciplinas" :key="'disc_'+disc.id" style="margin-bottom: 15px"> 
			<div v-for="aluno,index_aluno in disc.get_alunos" :key="'al_'+aluno.id"  style="margin-bottom:15px">
				<div>
					[[disc.descricao]] - [[aluno.matricula]] [[aluno.nome]]
					<button @click="deleteDisciplina(disc)">Excluir</button>
				</div>
			</div>
		</div>
		<div>
			<form action="">
				<input type="text" placeholder="Disciplina" v-model="novaDisciplina.descricao"/>
				<select multiple placeholder="Alunos" v-model="novaDisciplina.alunos"/>
					<option :key="aluno.id" v-for="aluno in alunos" :value="aluno.id">[[aluno.nome]]</option>}
				</select>
				<button @click="postNovaDisciplina()">Adicionar</button>
			</form>
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
				alunos: [],
				disciplinas: [],
				novaNacionalidade:{
					nome:'',
					pais:'',
					sigla:''
				},
				novoAluno:{
					nome:null,
					matricula:null,
					nacionalidade:null
				},
				novaDisciplina:{
					descricao:null,
					alunos:[],
				},

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
			},
			postNacionalidade(){
				this.$http.post('/nacionalidades/',this.novaNacionalidade).then(response => {
					if (response.ok){
						this.getNacionalidades()
					}
					this.novaNacionalidade = {
						nome:'', pais:'', sigla:''
					}
				  }).catch( error => {
					console.log('Error', error)
					alert(error.bodyText)
				  });
			},
			deleteNacionalidade(objeto){
				this.$http.delete(objeto.rud_url).then(response => {
					if (response.ok){
						this.getNacionalidades()
					}
					console.log(response)
				  }).catch( error => {
					console.log('Error', error)
					alert(error.bodyText)
				  })	
			},
			deleteAluno(objeto){
				this.$http.delete(objeto.rud_url).then(response => {
					if (response.ok){
						this.getAlunos()
					}
					console.log(response)
				  }).catch( error => {
					console.log('Error', error)
					alert(error.bodyText)
				  })
			},
			getAlunos(){
				console.log('Requisição de alunos')
				this.$http.get('/alunos/').then(response => {
					this.alunos = response.data;
					console.log('alunos', this.alunos)
				  }).catch( error => {
					this.alunos = []
					console.log('Error', error)
				  });
			},
			postNovoAluno(){
				console.log("Requisiçao de alunos")
				this.$http.post('/alunos/',this.novoAluno).then(response =>{
					if (response.ok){
						this.getAlunos()
						this.novoAluno={
							nome:null,
							matricula:null,
							nacionalidade:null
						}
					}
				}).catch( error =>{
					console.log('Error', error)
					alert(error)
				})
			},

			postNovaDisciplina(){
				console.log("Requisiçao de disciplinas")
				/*
				*/
				this.$http.post('/disciplinas/',this.novaDisciplina).then(response =>{
					if (response.ok){
						this.getDisciplina()
						this.novaDisciplina={
							descricao:null,
							alunos:[],
						}

					}
				}).catch( error =>{
					console.log('Error', error)
					alert(error)
				})
			},

			deleteDisciplina(objeto){
				this.$http.delete(objeto.rud_url).then(response =>{
					if (response.ok){
						this.getDisciplina()
					}
				}).catch( error =>{
					console.log('Error', error)
					alert(error)
				})
			},

			getDisciplina(){
				console.log('Requisição de disciplina')
				this.$http.get('/disciplinas/').then(response => {
					this.disciplinas	 = response.body;
					console.log('disciplinas', this.disciplinas)
				  }).catch( error => {
					this.disciplinas = []
					console.log('Error', error)
				  });
			},
			init(){
				this.getNacionalidades()
				this.getAlunos()
				this.getDisciplina()
			}
		},
		mounted(){
			this.init()
		},
		created(){
		},
		computed:{
			
		},
		watch:{
		}
	});
</script>