<script>

	import Graficos from './Graficos.svelte';

</script>

<main>
	<h1>Visualización de datos</h1>
	<Graficos />
</main>

<style>
	main {
		text-align: center;
		padding: 1em;
		max-width: 240px;
		margin: 0 auto;
	}

	h1 {
		color: #F7374F;
		text-transform: uppercase;
		font-size: 4em;
		font-weight: 500;
		text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
		padding-bottom: 2.5em;
	}

	@media (min-width: 640px) {
		main {
			max-width: none;
		}
	}
</style>