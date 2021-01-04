@extends('layouts.app')

@section('content')
<div class="container">
    <div class="row">
        <div class="col-12 pt-4">
            <div><h3>{{ $user->username }}</h3></div>
            <div class="pb-2">Books for sale: <strong>{{ count($user->books) }}</strong></div>
            <div class="pb-3">Email: {{ $user->email }}</div>
            @if(auth()->user() && (auth()->user()->id === $user->id))
            <a href="/b/create">Adauga anunt</a>
            @endif
        </div>
    </div>

    <div class="row pt-5">
        @foreach($user->books as $book)
            <div class="col-3 pt-5">
                <p><strong>Price: {{ $book->price }}</strong></p>
                <img src="/storage/{{ $book->image }}" class="w-100">
            </div>
        @endforeach
    </div>
</div>
@endsection
