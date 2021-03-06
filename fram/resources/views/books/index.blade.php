@extends('layouts.header')

@section('content')
    <div class="container">
        <div class="row">
            @if(count($books) === 0)
                <div>No results found for: <strong>{{ $searchedTerm }}</strong></div>
            @endif

            @foreach($books as $book)
                <div class="col-3 pt-5">
                    <div><strong>Seller: <a href="/profile/{{ $book->user_id }}">{{ $book->user->username }}</a> </strong></div>
                    <div><strong>Price: {{ $book->price }}</strong></div>
                    <img src="/storage/{{ $book->image }}" class="w-100">
                </div>
            @endforeach
        </div>
    </div>
@endsection

