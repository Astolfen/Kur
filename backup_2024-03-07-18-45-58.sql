PGDMP  :    -                |            cursach    16.0    16.0 4    �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            �           1262    17075    cursach    DATABASE     |   CREATE DATABASE cursach WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'English_Austria.1252';
    DROP DATABASE cursach;
                postgres    false            �            1259    17269    actor    TABLE     �   CREATE TABLE public.actor (
    id_actor integer NOT NULL,
    name_actor character varying(100) NOT NULL,
    age_actor integer NOT NULL
);
    DROP TABLE public.actor;
       public         heap    postgres    false            �            1259    17268    actor_id_actor_seq    SEQUENCE     �   CREATE SEQUENCE public.actor_id_actor_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 )   DROP SEQUENCE public.actor_id_actor_seq;
       public          postgres    false    225            �           0    0    actor_id_actor_seq    SEQUENCE OWNED BY     I   ALTER SEQUENCE public.actor_id_actor_seq OWNED BY public.actor.id_actor;
          public          postgres    false    224            �            1259    17181    genres    TABLE     p   CREATE TABLE public.genres (
    id_genres integer NOT NULL,
    name_genres character varying(100) NOT NULL
);
    DROP TABLE public.genres;
       public         heap    postgres    false            �            1259    17180    genres_id_genres_seq    SEQUENCE     �   CREATE SEQUENCE public.genres_id_genres_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 +   DROP SEQUENCE public.genres_id_genres_seq;
       public          postgres    false    216            �           0    0    genres_id_genres_seq    SEQUENCE OWNED BY     M   ALTER SEQUENCE public.genres_id_genres_seq OWNED BY public.genres.id_genres;
          public          postgres    false    215            �            1259    17197    genres_movie    TABLE     d   CREATE TABLE public.genres_movie (
    movie_id integer NOT NULL,
    genres_id integer NOT NULL
);
     DROP TABLE public.genres_movie;
       public         heap    postgres    false            �            1259    17189    movie    TABLE     �   CREATE TABLE public.movie (
    id_movie integer NOT NULL,
    name_movie character varying(100) NOT NULL,
    release_year integer NOT NULL,
    description character varying(500) NOT NULL
);
    DROP TABLE public.movie;
       public         heap    postgres    false            �            1259    17188    movie_id_movie_seq    SEQUENCE     �   CREATE SEQUENCE public.movie_id_movie_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 )   DROP SEQUENCE public.movie_id_movie_seq;
       public          postgres    false    218            �           0    0    movie_id_movie_seq    SEQUENCE OWNED BY     I   ALTER SEQUENCE public.movie_id_movie_seq OWNED BY public.movie.id_movie;
          public          postgres    false    217            �            1259    17250 
   play_movie    TABLE     a   CREATE TABLE public.play_movie (
    movie_id integer NOT NULL,
    actor_id integer NOT NULL
);
    DROP TABLE public.play_movie;
       public         heap    postgres    false            �            1259    17221    user    TABLE     �   CREATE TABLE public."user" (
    name_user character varying(50) NOT NULL,
    password_user character varying(50) NOT NULL,
    role_user integer NOT NULL
);
    DROP TABLE public."user";
       public         heap    postgres    false            �            1259    17215 	   user_role    TABLE     n   CREATE TABLE public.user_role (
    id_role integer NOT NULL,
    name_role character varying(50) NOT NULL
);
    DROP TABLE public.user_role;
       public         heap    postgres    false            �            1259    17214    user_role_id_role_seq    SEQUENCE     �   CREATE SEQUENCE public.user_role_id_role_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 ,   DROP SEQUENCE public.user_role_id_role_seq;
       public          postgres    false    221            �           0    0    user_role_id_role_seq    SEQUENCE OWNED BY     O   ALTER SEQUENCE public.user_role_id_role_seq OWNED BY public.user_role.id_role;
          public          postgres    false    220            8           2604    17272    actor id_actor    DEFAULT     p   ALTER TABLE ONLY public.actor ALTER COLUMN id_actor SET DEFAULT nextval('public.actor_id_actor_seq'::regclass);
 =   ALTER TABLE public.actor ALTER COLUMN id_actor DROP DEFAULT;
       public          postgres    false    224    225    225            5           2604    17184    genres id_genres    DEFAULT     t   ALTER TABLE ONLY public.genres ALTER COLUMN id_genres SET DEFAULT nextval('public.genres_id_genres_seq'::regclass);
 ?   ALTER TABLE public.genres ALTER COLUMN id_genres DROP DEFAULT;
       public          postgres    false    216    215    216            6           2604    17192    movie id_movie    DEFAULT     p   ALTER TABLE ONLY public.movie ALTER COLUMN id_movie SET DEFAULT nextval('public.movie_id_movie_seq'::regclass);
 =   ALTER TABLE public.movie ALTER COLUMN id_movie DROP DEFAULT;
       public          postgres    false    218    217    218            7           2604    17218    user_role id_role    DEFAULT     v   ALTER TABLE ONLY public.user_role ALTER COLUMN id_role SET DEFAULT nextval('public.user_role_id_role_seq'::regclass);
 @   ALTER TABLE public.user_role ALTER COLUMN id_role DROP DEFAULT;
       public          postgres    false    221    220    221            �          0    17269    actor 
   TABLE DATA           @   COPY public.actor (id_actor, name_actor, age_actor) FROM stdin;
    public          postgres    false    225   K8       �          0    17181    genres 
   TABLE DATA           8   COPY public.genres (id_genres, name_genres) FROM stdin;
    public          postgres    false    216   �8       �          0    17197    genres_movie 
   TABLE DATA           ;   COPY public.genres_movie (movie_id, genres_id) FROM stdin;
    public          postgres    false    219   9       �          0    17189    movie 
   TABLE DATA           P   COPY public.movie (id_movie, name_movie, release_year, description) FROM stdin;
    public          postgres    false    218   <9       �          0    17250 
   play_movie 
   TABLE DATA           8   COPY public.play_movie (movie_id, actor_id) FROM stdin;
    public          postgres    false    223   g<       �          0    17221    user 
   TABLE DATA           E   COPY public."user" (name_user, password_user, role_user) FROM stdin;
    public          postgres    false    222   �<       �          0    17215 	   user_role 
   TABLE DATA           7   COPY public.user_role (id_role, name_role) FROM stdin;
    public          postgres    false    221   �<       �           0    0    actor_id_actor_seq    SEQUENCE SET     @   SELECT pg_catalog.setval('public.actor_id_actor_seq', 3, true);
          public          postgres    false    224            �           0    0    genres_id_genres_seq    SEQUENCE SET     B   SELECT pg_catalog.setval('public.genres_id_genres_seq', 7, true);
          public          postgres    false    215            �           0    0    movie_id_movie_seq    SEQUENCE SET     A   SELECT pg_catalog.setval('public.movie_id_movie_seq', 22, true);
          public          postgres    false    217            �           0    0    user_role_id_role_seq    SEQUENCE SET     D   SELECT pg_catalog.setval('public.user_role_id_role_seq', 1, false);
          public          postgres    false    220            M           2606    17274    actor actor_pkey 
   CONSTRAINT     T   ALTER TABLE ONLY public.actor
    ADD CONSTRAINT actor_pkey PRIMARY KEY (id_actor);
 :   ALTER TABLE ONLY public.actor DROP CONSTRAINT actor_pkey;
       public            postgres    false    225            ?           2606    17201    genres_movie genres_movie_pkey 
   CONSTRAINT     m   ALTER TABLE ONLY public.genres_movie
    ADD CONSTRAINT genres_movie_pkey PRIMARY KEY (movie_id, genres_id);
 H   ALTER TABLE ONLY public.genres_movie DROP CONSTRAINT genres_movie_pkey;
       public            postgres    false    219    219            ;           2606    17186    genres genres_pkey 
   CONSTRAINT     W   ALTER TABLE ONLY public.genres
    ADD CONSTRAINT genres_pkey PRIMARY KEY (id_genres);
 <   ALTER TABLE ONLY public.genres DROP CONSTRAINT genres_pkey;
       public            postgres    false    216            =           2606    17196    movie movie_pkey 
   CONSTRAINT     T   ALTER TABLE ONLY public.movie
    ADD CONSTRAINT movie_pkey PRIMARY KEY (id_movie);
 :   ALTER TABLE ONLY public.movie DROP CONSTRAINT movie_pkey;
       public            postgres    false    218            H           2606    17254    play_movie play_movie_pkey 
   CONSTRAINT     h   ALTER TABLE ONLY public.play_movie
    ADD CONSTRAINT play_movie_pkey PRIMARY KEY (movie_id, actor_id);
 D   ALTER TABLE ONLY public.play_movie DROP CONSTRAINT play_movie_pkey;
       public            postgres    false    223    223            E           2606    17225    user user_pkey 
   CONSTRAINT     U   ALTER TABLE ONLY public."user"
    ADD CONSTRAINT user_pkey PRIMARY KEY (name_user);
 :   ALTER TABLE ONLY public."user" DROP CONSTRAINT user_pkey;
       public            postgres    false    222            C           2606    17220    user_role user_role_pkey 
   CONSTRAINT     [   ALTER TABLE ONLY public.user_role
    ADD CONSTRAINT user_role_pkey PRIMARY KEY (id_role);
 B   ALTER TABLE ONLY public.user_role DROP CONSTRAINT user_role_pkey;
       public            postgres    false    221            K           1259    17275    actor_name_actor    INDEX     O   CREATE UNIQUE INDEX actor_name_actor ON public.actor USING btree (name_actor);
 $   DROP INDEX public.actor_name_actor;
       public            postgres    false    225            9           1259    17187    genres_name_genres    INDEX     S   CREATE UNIQUE INDEX genres_name_genres ON public.genres USING btree (name_genres);
 &   DROP INDEX public.genres_name_genres;
       public            postgres    false    216            @           1259    17213    genresmovie_genres_id    INDEX     S   CREATE INDEX genresmovie_genres_id ON public.genres_movie USING btree (genres_id);
 )   DROP INDEX public.genresmovie_genres_id;
       public            postgres    false    219            A           1259    17212    genresmovie_movie_id    INDEX     Q   CREATE INDEX genresmovie_movie_id ON public.genres_movie USING btree (movie_id);
 (   DROP INDEX public.genresmovie_movie_id;
       public            postgres    false    219            I           1259    17266    playmovie_actor_id    INDEX     M   CREATE INDEX playmovie_actor_id ON public.play_movie USING btree (actor_id);
 &   DROP INDEX public.playmovie_actor_id;
       public            postgres    false    223            J           1259    17265    playmovie_movie_id    INDEX     M   CREATE INDEX playmovie_movie_id ON public.play_movie USING btree (movie_id);
 &   DROP INDEX public.playmovie_movie_id;
       public            postgres    false    223            F           1259    17231    user_role_user    INDEX     F   CREATE INDEX user_role_user ON public."user" USING btree (role_user);
 "   DROP INDEX public.user_role_user;
       public            postgres    false    222            N           2606    17207 (   genres_movie genres_movie_genres_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.genres_movie
    ADD CONSTRAINT genres_movie_genres_id_fkey FOREIGN KEY (genres_id) REFERENCES public.genres(id_genres);
 R   ALTER TABLE ONLY public.genres_movie DROP CONSTRAINT genres_movie_genres_id_fkey;
       public          postgres    false    4667    219    216            O           2606    17202 '   genres_movie genres_movie_movie_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.genres_movie
    ADD CONSTRAINT genres_movie_movie_id_fkey FOREIGN KEY (movie_id) REFERENCES public.movie(id_movie);
 Q   ALTER TABLE ONLY public.genres_movie DROP CONSTRAINT genres_movie_movie_id_fkey;
       public          postgres    false    4669    218    219            Q           2606    17255 #   play_movie play_movie_movie_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.play_movie
    ADD CONSTRAINT play_movie_movie_id_fkey FOREIGN KEY (movie_id) REFERENCES public.movie(id_movie);
 M   ALTER TABLE ONLY public.play_movie DROP CONSTRAINT play_movie_movie_id_fkey;
       public          postgres    false    4669    218    223            P           2606    17226    user user_role_user_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public."user"
    ADD CONSTRAINT user_role_user_fkey FOREIGN KEY (role_user) REFERENCES public.user_role(id_role);
 D   ALTER TABLE ONLY public."user" DROP CONSTRAINT user_role_user_fkey;
       public          postgres    false    221    4675    222            �   P   x�ȱ� @��n
&01R�.��`%�PH�1�
�6�W�Q�d�d7�qP8I|=
M�����<W�j;/ق�Y�AU��*       �   T   x����0�w2`������*yP)����l�<	nT4t�̰h��������<t�/�k�̺HZ�B�oW\Ӡ�/��2�      �      x�32�4�22�4�\FF@"F��� -AO      �     x�]TKnA\ۧ�+����9�'#�H1�#!$bÂ͌�vƞ�����'����,y���U��泑��&�Xe�5v�./_�샳������5���ּ����z�g�۸x�V!�G�ւ{��~��[g�X�x����~q퐘����w<(W�����X��6�VǕ�Ox�vd���H��@o`q	�&�*	�".�Y�_oM����<�G��Ii7(�f΄y�['��Z,'..�0�9��!�u �����a��D��`'$�!e �`���oj> ;W�6ޣd)�*1�io�����H��h�lӓ�6��+[4��������������&�慫��G<���%n+t]�@Z��,6��x�6x`b�L������$v)�I�N��+��@B����}CSK*oa4��]��+����Y|t�Ϩ��h�M�����rd|�=��PM�>/~�@V�+��h�}b��zp.�w�F��3a�L{Y9S�\z����"$A�s��]�)��r���
N�&!"`���F�NR�ּy�)A3�h��r��t�j/�4ۙfV,4����EZ��K޴�A8;{��@����+ksE=G>�KnGCc�		�Ԧ"���ᄤA��ELO�� `�!ڋB�h�!VR�gPz�e���������	��������4��A�����ھ�I�p�焊�������bX�t��A��N% ���p����e�B:5�|%�N=����N������h\|��T~� p�<p�I���@J���t<�\_[      �      x�32�4�22�4�22�b���� V�      �   +   x�KL����L��\�ũE�`��6ℐF\���@2F��� ���      �      x�3�LL����2�,-N-����� : �     