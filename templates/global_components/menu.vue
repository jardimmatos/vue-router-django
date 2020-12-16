<template id="component_menu">
	<div>
		<span><router-link to="/login">Login </router-link> |</span>
		<span><router-link to="/">Home </router-link> |</span>
		<span><router-link to="/alunos">Alunos </router-link> |</span>
		<span v-for="menu, index in menus" key="index"><a :href="menu.link"> [[menu.label]] [[ index + 1 ]]</a> |</span>
	</div>
</template>

<script type="text/javascript">
	
	Vue.component('my-menu',{
		template: '#component_menu',
		props: {
		},
		delimiters: ['[[',']]'],
		//vuetify: new Vuetify({}),
		data(){
			return {
				menus:[
					{ label:'Menu', link:'#' },
					{ label:'Menu', link:'#' },
					{ label:'Menu', link:'#' },
					{ label:'Menu', link:'#' },
				]
			}
		},
		methods:{
		},
		mounted(){
		},
		created(){
		},
		computed:{
		},
		watch:{
		}
	});
</script>